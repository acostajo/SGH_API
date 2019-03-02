from rest_framework import serializers
from orinasimpledatoslab.models import OrinaSimpleDL

class OrinaSimpleDLSerializer(serializers.ModelSerializer):
    """Orina simple class."""
    class Meta:
        model = OrinaSimpleDL
        fields = ('codorinadl', 'codorina', 'codorinadl')
