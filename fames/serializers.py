from rest_framework import serializers
from e.models import Fames  

class FamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fames
        fields = ('codfame
        'codusuario',
        'nombre',
        'fechacreada')