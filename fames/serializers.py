from rest_framework import serializers
from fames.models import Fames  

class FamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fames
        fields = ('codfame',
        'codusuario',
        'nombre',
        'fechacreada')