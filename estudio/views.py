from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Estudio
from .serializers import EstudioSerializer
import json

@csrf_exempt
def efectoadversoconsulta_list(request):
    """
    Lista todas los efectos adeversos asosciado con consulta
    """
    if request.method == 'POST':
        x = json.loads(request)
        print(x)
        




