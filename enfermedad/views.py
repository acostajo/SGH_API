from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from enfermedad.models import Enfermedad
from enfermedad.serializers import EnfermedadSerializer

@csrf_exempt
def enfermedad_list(request):
    """ Lista todas las Enfermedades  """
    if request.method == 'GET':
        enfermedades = Enfermedad.objects.all()
        serializer = EnfermedadSerializer(enfermedades, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EnfermedadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def enfermedad_detail(request, pk):
    """
    recupera, actualiza o elimina una ficha
    """
    try:
        enfermedad = Enfermedad.objects.get(pk=pk)
    except Enfermedad.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EnfermedadSerializer(enfermedad)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EnfermedadSerializer(enfermedad, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        enfermedad.delete()
        return HttpResponse(status=204)