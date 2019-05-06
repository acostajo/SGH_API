from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ordenestudio.models import OrdenEstudio
from ordenestudio.serializers import OrdenEstudioSerializer


@csrf_exempt
def ordenestudio_list(request):
    """ Lista todas las fichas  """
    print(request.method)
    if request.method == "GET":
        ordenestudios = OrdenEstudio.objects.all()
        serializer = OrdenEstudioSerializer(ordenestudios, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = OrdenEstudioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def ordenestudio_detail(request, pk):
    """
    recupera, actualiza o elimina una ficha
    """
    try:
        ordenestudio = OrdenEstudio.objects.get(pk=pk)
    except OrdenEstudio.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = OrdenEstudioSerializer(ordenestudio)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = OrdenEstudioSerializer(ordenestudio, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        ordenestudio.delete()
        return HttpResponse(status=204)
