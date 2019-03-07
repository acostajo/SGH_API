from rest_framework import serializers
from enfermedad.models import Enfermedad


class EnfermedadSerializer(serializers.ModelSerializer):
    """Enfermedad simple class."""

    class Meta:
        model = Enfermedad
        fields = ("codenfermedad", "codusuario", "nombre", "fechacreada")
