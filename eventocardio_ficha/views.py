from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from eventocardio_ficha.models import EventoCardiovascularFicha
from eventocardio_ficha.serializers import EventoCardiovascularFichaSerializer

@csrf_exempt
def eventocardiovascularficha_list(request):
    """
    Lista todas los eventos cardiovasculares asociados a la ficha
    """
    if request.method == 'GET':
        eventocardiovascularfichas = EventoCardiovascularFicha.objects.all()
        serializer = EventoCardiovascularFichaSerializer(eventocardiovascularfichas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EventoCardiovascularFichaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def eventocardiovascularficha_detail(request, pk):
    """
    recupera, actualiza o elimina un evento cardiovascular asociado a la ficha
    """
    try:
        eventocardiovascularficha = EventoCardiovascualarFicha.objects.get(pk=pk)
    except eventocardiovascularficha.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EventoCardiovascularFichaSerializer(eventocardiovascularficha)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EventoCardiovascularFichaSerializer(eventocardiovascularficha, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        eventocardiovascularficha.delete()
        return HttpResponse(status=204)
