from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from orinasimpledatoslab.models import OrinaSimpleDL
from orinasimpledatoslab.serializers import OrinaSimpleDLSerializer

@csrf_exempt
def orinaDL_list(request):
    """ Lista todas las fichas  """
    if request.method == 'GET':
        orinasDL = OrinaSimpleDL.objects.all()
        serializer = OrinaSimpleDLSerializer(orinasDL, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrinaSimpleDLSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def orinaDL_detail(request, pk):
    """
    recupera, actualiza o elimina una ficha
    """
    try:
        orinasDL = OrinaSimpleDL.objects.get(pk=pk)
    except OrinaSimpleDL.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrinaSimpleDLSerializer(orinasDL)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrinaSimpleDLSerializer(orinasDL, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        orinasDL.delete()
        return HttpResponse(status=204)
