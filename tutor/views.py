from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import gerar_resposta_ia

@api_view(['POST'])
def tutor_chat(request):
    try:
        mensagem = request.data.get('mensagem', '')
        if not mensagem:
            return Response({"error": "O campo 'mensagem' é obrigatório."}, status=400)

        resposta = gerar_resposta_ia(mensagem)
        return Response({"resposta": resposta})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
