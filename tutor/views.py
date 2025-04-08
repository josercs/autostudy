from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .utils import gerar_resposta_ia
from .models import StudyPlan
from .serializers import StudyPlanSerializer

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

class StudyPlanViewSet(viewsets.ModelViewSet):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retorna apenas os planos de estudo do usuário autenticado
        return self.queryset.filter(user=self.request.user)
