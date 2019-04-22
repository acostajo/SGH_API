from rest_framework import serializers
from enfermedad.models import Enfermedad


class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedad
        fields = '__all__'
