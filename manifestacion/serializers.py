from rest_framework import serializers
from e.models import Manifestacion  

class ManifestacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manifestacion
        fields = ('codmanifficha',
        'codmanif',
        'codficha') 