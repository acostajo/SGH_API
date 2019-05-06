from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from fames.models import Fames
from fames.serializers import FamesSerializer

@csrf_exempt
def fames_list(request):
    """
    Lista todas los fames 
    """
    
    if request.method == 'GET':
        famess = Fames.objects.all()
        serializer = FamesSerializer(famess, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FamesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def fames_detail(request, pk):
    """
    recupera, actualiza o elimina un fames 
    """
    try:
        fames = Fames.objects.get(pk=pk)
    except Fames.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FamesSerializer(fames)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FamesSerializer(fames, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        fames.delete()
        return HttpResponse(status=204)
