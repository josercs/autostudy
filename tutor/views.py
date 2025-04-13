from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .utils import gerar_resposta_ia
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tutor_chat(request):
    try:
        logger.info(f"Request data: {request.data}")
        mensagem = request.data.get('mensagem', '').strip()

        if not mensagem:
            return Response(
                {"error": "Mensagem não pode estar vazia"},
                status=status.HTTP_400_BAD_REQUEST
            )

        resposta = gerar_resposta_ia(mensagem)
        logger.info(f"Resposta gerada: {resposta[:200]}...")  # Log parcial

        return Response(
            {"resposta": resposta},
            status=status.HTTP_200_OK,
            content_type='application/json; charset=utf-8'
        )

    except Exception as e:
        logger.error(f"ERRO CRÍTICO: {str(e)}", exc_info=True)
        return Response(
            {
                "error": "Erro interno do servidor",
                "detalhes": str(e)
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )