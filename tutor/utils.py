import google.generativeai as genai
import os
from django.conf import settings
from google.api_core import retry

class GeminiTutor:
    def __init__(self):
        self.model = None
        self._initialize()

    def _initialize(self):
        try:
            api_key = settings.GOOGLE_API_KEY
            if not api_key:
                raise ValueError("Chave API não configurada")
            
            genai.configure(api_key=api_key)
            
            # Especificando explicitamente o modelo 1.5 pro latest
            self.model = genai.GenerativeModel('gemini-1.5-pro-latest')
            
            # Teste de saúde do modelo
            test_response = self.model.generate_content(
                "Teste de conexão com o modelo",
                generation_config={
                    "temperature": 0.7,
                    "max_output_tokens": 2000
                }
            )
            
            if not test_response.text:
                raise ValueError("Resposta de teste vazia")
                
        except Exception as e:
            print(f"Falha na inicialização do Gemini: {str(e)}")
            self.model = None

    @retry.Retry()  # Adiciona retry automático para falhas transitórias
    def generate_response(self, prompt):
        if not self.model:
            return "Serviço temporariamente indisponível"

        try:
            response = self.model.generate_content(
                {
                    "parts": [{
                        "text": f"Como tutor educacional, responda em português brasileiro de forma clara e detalhada:\n\n{prompt}"
                    }],
                },
                generation_config={
                    "temperature": 0.7,
                    "max_output_tokens": 2000,
                    "top_p": 0.9,
                    "top_k": 40
                }
            )
            
            if not response.text:
                raise ValueError("Resposta vazia da API")
                
            return response.text.strip()
            
        except Exception as e:
            print(f"Erro na geração de resposta: {str(e)}")
            return f"Resposta padrão sobre: {prompt[:50]}... (erro: {str(e)})"

# Instância global do tutor
tutor = GeminiTutor()

def gerar_resposta_ia(mensagem):
    return tutor.generate_response(mensagem)