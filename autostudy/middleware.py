import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as ex:
            logger.error(f"Erro não tratado: {str(ex)}")
            response = JsonResponse({'error': 'Erro interno do servidor'}, status=500)
        return response