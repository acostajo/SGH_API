from rest_framework import serializers
from orinasimple.models import OrinaSimple

class OrinaSimpleSerializer(serializers.ModelSerializer):
    """Orina simple class."""
    class Meta:
        model = OrinaSimple
        fields = ('codorina', 'codusuario', 'nombre', 'fechacreada')
