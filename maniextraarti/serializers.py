from rest_framework import serializers
from e.models import ManiExtraArti  

class ManiExtraArtiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManiExtraArti
        fields = ('codmanif',
        'codusuario',
        'nombre',
        'descripcion',
        'fechacreada')