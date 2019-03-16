from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from panolab.models import Panolab
from panolab.serializers import PanolabSerializer


@csrf_exempt
def panolab_list(request):
    """
    Lista todas las panoramicas de laboratorio 
    """
    if request.method == 'GET':
        panolabs = Panolab.objects.all()
        serializer = PanolabSerializer(panolabs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PanolabSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def panolab_detail(request, pk):
    """
    recupera, actualiza o elimina una panoramicas de laboratorio 
    """
    try:
        panolab = Panolab.objects.get(pk=pk)
    except Panolab.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PanolabSerializer(panolab)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PanolabSerializer(panolab, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        panolab.delete()
        return HttpResponse(status=204)
