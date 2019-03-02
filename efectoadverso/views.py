from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from efectoadverso.models import EfectoAdverso
from efectoadverso.serializers import EfectoAdversoSerializer

@csrf_exempt
def efectoadverso_list(request):
    """
    Lista todas los efectos adeversos
    """
    if request.method == 'GET':
        efectoadversos = EfectoAdverso.objects.all()
        serializer = EfectoAdversoSerializer(efectoadversos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EfectoAdversoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def efectoadverso_detail(request, pk):
    """
    recupera, actualiza o elimina un efecto adverso
    """
    try:
        efectoadverso = EfectoAdverso.objects.get(pk=pk)
    except EfectoAdverso.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EfectoAdversoSerializer(efectoadverso)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EfectoAdversoSerializer(efectoadverso, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        efectoadverso.delete()
        return HttpResponse(status=204)
