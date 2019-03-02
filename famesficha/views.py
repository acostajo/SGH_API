from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from famesficha.models import FamesFicha
from famesficha.serializers import FamesFichaSerializer

@csrf_exempt
def famesficha_list(request):
    """
    Lista todas los fames asociado a una ficha
    """
    if request.method == 'GET':
        famesfichas = FamesFicha.objects.all()
        serializer = FamesFichaSerializer(famesfichas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FamesFichaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def famesficha_detail(request, pk):
    """
    recupera, actualiza o elimina un fames asociado a una ficha
    """
    try:
        famesficha = FamesFicha.objects.get(pk=pk)
    except FamesFicha.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FamesFichaSerializer(famesficha)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FamesFichaSerializer(famesficha, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        famesficha.delete()
        return HttpResponse(status=204)
