from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from efectoadverso_consulta.models import EfectoAdversoConsulta
from efectoadverso_consulta.serializers import EfectoAdversoConsultaSerializer

@csrf_exempt
def efectoadversoconsulta_list(request):
    """
    Lista todas los efectos adeversos asosciado con consulta
    """
    if request.method == 'GET':
        efectoadversoconsultas = EfectoAdversoConsulta.objects.all()
        serializer = EfectoAdversoConsultaSerializer(efectoadversoconsultas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EfectoAdversoConsultaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def efectoadversoconsulta_detail(request, pk):
    """
    recupera, actualiza o elimina un efecto adverso asosciado con consulta
    """
    try:
        efectoadversoconsulta = EfectoAdversoConsulta.objects.get(pk=pk)
    except EfectoAdversoConsulta.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EfectoAdversoConsultaSerializer(efectoadversoconsulta)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EfectoAdversoConsultaSerializer(efectoadversoconsulta, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        efectoadversoconsulta.delete()
        return HttpResponse(status=204)
