from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

def process_message_with_ai(message):
    # Integração com a API de IA, por exemplo, chamando o OpenAI ou outro serviço.
    # Por enquanto, retorna uma resposta simulada.
    return f"Resposta simulada para a mensagem: {message}"

class ChatbotAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user_message = request.data.get('message')
        if not user_message:
            return Response({'error': 'Mensagem não fornecida.'}, status=400)
        bot_response = process_message_with_ai(user_message)
        return Response({'response': bot_response})
