from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from consulta.models import Consulta
from consulta.serializers import ConsultaSerializer

@csrf_exempt
def consulta_list(request):
    """
    Lista todas las consultas 
    """
    if request.method == 'GET':
        consultas = Consulta.objects.all()
        serializer = ConsultaSerializer(consultas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ConsultaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def consulta_detail(request, pk):
    """
    recupera, actualiza o elimina una consulta
    """
    try:
        consulta = Consulta.objects.get(pk=pk)
    except Consulta.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ConsultaSerializer(consulta)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ConsultaSerializer(consulta, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        consulta.delete()
        return HttpResponse(status=204)
