import google.generativeai as genai
import os
import logging

logger = logging.getLogger('utils')  # Logger configurado no settings.py

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def gerar_resposta_ia(mensagem):
    try:
        MODELO_PADRAO = 'models/gemini-1.5-flash-latest'
        try:
            model = genai.GenerativeModel(MODELO_PADRAO)
            resposta = model.generate_content(
                mensagem,
                generation_config={
                    "temperature": 0.7,
                    "max_output_tokens": 200,
                }
            )
            return resposta.text
        except Exception as e:
            logger.error(f"Modelo padrão não disponível: {str(e)}")
            logger.info("Fazendo fallback para busca automática de modelos...")

            modelos_disponiveis = [m for m in genai.list_models() 
                                   if 'generateContent' in m.supported_generation_methods]

            if not modelos_disponiveis:
                logger.error("Nenhum modelo compatível encontrado.")
                return "Nenhum modelo compatível encontrado"

            modelo_usar = modelos_disponiveis[0].name
            logger.info(f"Usando modelo alternativo: {modelo_usar}")

            model = genai.GenerativeModel(modelo_usar)
            resposta = model.generate_content(
                mensagem,
                generation_config={
                    "temperature": 0.7,
                    "max_output_tokens": 200,
                }
            )
            return resposta.text
    except Exception as e:
        logger.error(f"Erro ao processar a mensagem: {str(e)}")
        return f"Erro ao processar a mensagem: {str(e)}"