from rest_framework import serializers
from estudio.models import Estudio


class EstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudio
        fields = "__all__"

