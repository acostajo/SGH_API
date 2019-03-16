from rest_framework import serializers
from panolab.models import Panolab


class PanolabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panolab
        fields = '__all__'

# asi se exporta todo
