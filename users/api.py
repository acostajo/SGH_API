
from django_filters.rest_framework import DjangoFilterBackend
from .models import User
from rest_framework import viewsets, permissions
from .serializers import CustomUserDetailsSerializer  # este nomas era


class UserViewSet(viewsets.ModelViewSet):
    # en este obtenemos todos los objetos que hay en la bd
    queryset = User.objects.all()
    # estos son los permisos, si implementamos usuario vamos a usar, por el momento usamos este nomas
    permission_classes = [permissions.AllowAny]
    # este s la clase serializer que creamos la ves pasada
    serializer_class = CustomUserDetailsSerializer
    # este es algo que requiere el django para que funcione el filtro
    filter_backends = (DjangoFilterBackend,)
    # estos son los filtros, aca asignamos los campos de la base de datos por el cual vamos a buscar los objetos
    filter_fields = ("tipo", "username")