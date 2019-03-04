from .models import Ficha, Paciente
from rest_framework import viewsets, permissions
from .serializers import FichaSerializer, PacienteSerializer


class FichaViewSet(viewsets.ModelViewSet):
    queryset = Ficha.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FichaSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacienteSerializer
