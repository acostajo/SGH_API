from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from agenda.models import Agenda
from agenda.serializers import AgendaSerializer


@csrf_exempt
def agenda_list(request):
    """ Lista todas las agenda  """
    print(request)
    if request.method == "GET":
        agendas = Enfermedad.objects.all()
        serializer = AgendaSerializer(agendas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        serializer = AgendaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def agenda_detail(request, pk):
    """
    recupera, actualiza o elimina una ficha
    """
    try:
        agenda = Agenda.objects.get(pk=pk)
    except Agenda.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = AgendaSerializer(agenda)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = AgendaSerializer(agenda, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        agenda.delete()
        return HttpResponse(status=204)
