import google.generativeai as genai
import os

# Configura a chave da API do Google
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def gerar_resposta_ia(mensagem, max_tokens=8192):
    try:
        MODELO_PADRAO = os.getenv("GOOGLE_DEFAULT_MODEL", "models/gemini-1.5-flash-latest")
        model = genai.GenerativeModel(MODELO_PADRAO)
        
        response = model.generate_content(
            mensagem,
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": max_tokens,
                "top_p": 0.95,
                "top_k": 40
            },
            safety_settings={
                "HARASSMENT": "BLOCK_NONE",
                "HATE_SPEECH": "BLOCK_NONE",
                "SEXUAL": "BLOCK_NONE",
                "DANGEROUS": "BLOCK_NONE"
            }
        )
        return response.text
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"