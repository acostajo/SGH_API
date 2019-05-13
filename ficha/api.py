from django_filters.rest_framework import DjangoFilterBackend
from .models import Ficha
from rest_framework import viewsets, permissions
from .serializers import FichaSerializer


class FichaViewSet(viewsets.ModelViewSet):
    queryset = Ficha.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FichaSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("nrodocumento", "codficha","nombres","apellidos",)
    
