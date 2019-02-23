from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ficha.models import Ficha
from ficha.serializers import FichaSerializer

@csrf_exempt
def ficha_list(request):
    """
    Lista todas las fichas 
    """
    if request.method == 'GET':
        fichas = Ficha.objects.all()
        serializer = FichaSerializer(fichas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FichaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def ficha_detail(request, pk):
    """
    recupera, actualiza o elimina una ficha
    """
    try:
        ficha = Ficha.objects.get(pk=pk)
    except Ficha.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FichaSerializer(ficha)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FichaSerializer(ficha, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ficha.delete()
        return HttpResponse(status=204)