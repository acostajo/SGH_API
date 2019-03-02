from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from maniextraarti.models import ManiExtraArti
from maniextraarti.serializers import ManiExtraArtiSerializer

@csrf_exempt
def maniextraarti_list(request):
    """
    Lista todas las manifestaciones extra articulares
    """
    if request.method == 'GET':
        maniextraartis = ManiExtraArti.objects.all()
        serializer = ManiExtraArtiSerializer(maniextraartis, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ManiExtraArtiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def maniextraarti_detail(request, pk):
    """
    recupera, actualiza o elimina una manifestacion
    """
    try:
        maniextraarti = ManiExtraArti.objects.get(pk=pk)
    except ManiExtraArti.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ManiExtraArtiSerializer(maniextraarti)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ManiExtraArtiSerializer(maniextraarti, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        maniextraarti.delete()
        return HttpResponse(status=204)
