from django_filters.rest_framework import DjangoFilterBackend
from .models import Panolab
from rest_framework import viewsets, permissions
from .serializers import PanolabSerializer  # este nomas era


class PanolabViewSet(viewsets.ModelViewSet):
    # en este obtenemos todos los objetos que hay en la bd
    queryset = Panolab.objects.all()
    # estos son los permisos, si implementamos usuario vamos a usar, por el momento usamos este nomas
    permission_classes = [permissions.AllowAny]
    # este s la clase serializer que creamos la ves pasada
    serializer_class = PanolabSerializer
    # este es algo que requiere el django para que funcione el filtro
    filter_backends = (DjangoFilterBackend,)
    # estos son los filtros, aca asignamos los campos de la base de datos por el cual vamos a buscar los objetos
    filter_fields = ("fechapanolab", "codficha","codpanolab",) 
