from rest_framework import serializers
from ordenestudio.models import OrdenEstudio


class OrdenEstudioSerializer(serializers.ModelSerializer):
    """Orden Estudio class."""

    class Meta:
        model = OrdenEstudio
        fields = '__all__'