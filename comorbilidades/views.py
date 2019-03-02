from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from comorbilidades.models import Comorbilidad
from comorbilidades.serializers import ComorbilidadSerializer

@csrf_exempt
def comorbilidad_list(request):
    """ Lista todas las Enfermedades  """
    if request.method == 'GET':
        comorbilidades = Comorbilidad.objects.all()
        serializer = ComorbilidadSerializer(comorbilidades, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ComorbilidadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def comorbilidad_detail(request, pk):
    """
    recupera, actualiza o elimina una ficha
    """
    try:
        comorbilidad = Comorbilidad.objects.get(pk=pk)
    except Comorbilidad.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ComorbilidadSerializer(comorbilidad)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ComorbilidadSerializer(comorbilidad, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        comorbilidad.delete()
        return HttpResponse(status=204)