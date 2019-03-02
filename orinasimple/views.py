from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from orinasimple.models import OrinaSimple
from orinasimple.serializers import OrinaSimpleSerializer

@csrf_exempt
def orina_list(request):
    """ Lista todas las fichas  """
    if request.method == 'GET':
        orinas = OrinaSimple.objects.all()
        serializer = OrinaSimpleSerializer(orinas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrinaSimpleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def orina_detail(request, pk):
    """
    recupera, actualiza o elimina una ficha
    """
    try:
        orina = OrinaSimple.objects.get(pk=pk)
    except OrinaSimple.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrinaSimpleSerializer(orina)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrinaSimpleSerializer(orina, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        orina.delete()
        return HttpResponse(status=204)
