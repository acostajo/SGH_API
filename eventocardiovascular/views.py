from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from eventocardiovascular.models import EventoCardiovascular
from eventocardiovascular.serializers import EventoCardiovascularSerializer

@csrf_exempt
def eventocardiovascular_list(request):
    """
    Lista todas los eventos cardiovasculares
    """
    if request.method == 'GET':
        eventocardiovasculares = EventoCardiovascular.objects.all()
        serializer = EventoCardiovascualarSerializer(eventocardiovasculares, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EventoCardiovascularSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def eventocardiovascular_detail(request, pk):
    """
    recupera, actualiza o elimina un evento cardiovascular
    """
    try:
        eventocardiovascular = EventoCardiovascular.objects.get(pk=pk)
    except eventocardiovascular.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EventoCardiovascualarSerializer(eventocardiovascular)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EventoCardiovascualarSerializer(eventocardiovascular, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        eventocardiovascular.delete()
        return HttpResponse(status=204)
