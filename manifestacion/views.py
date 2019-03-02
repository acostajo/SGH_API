from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from manifestacion.models import Manifestacion
from manifestacion.serializers import ManifestacionSerializer

@csrf_exempt
def manifestacion_list(request):
    """
    Lista todas las manifestaciones
    """
    if request.method == 'GET':
        manifestaciones = Manifestacion.objects.all()
        serializer = ManifestacionSerializer(manifestaciones, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ManifestacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def manifestacion_detail(request, pk):
    """
    recupera, actualiza o elimina una manifestacion
    """
    try:
        manifestacion = Manifestacion.objects.get(pk=pk)
    except Manifestacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ManifestacionSerializer(manifestacion)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ManifestacionSerializer(manifestacion, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        manifestacion.delete()
        return HttpResponse(status=204)
