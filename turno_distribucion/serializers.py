from rest_framework import serializers
from .models import TurnoDist


class TurnoDistSerializer(serializers.ModelSerializer):

    class Meta:
        model = TurnoDist
        fields = '__all__'
