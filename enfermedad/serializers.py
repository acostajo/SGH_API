from rest_framework import serializers
from enfermedad.models import Enfermedad

class EnfermedadSerializer(serializers.ModelSerializer):
    """Orina simple class."""
    class Meta:
        model = Enfermedad
        fields = ('codorina', 'codusuario', 'nombre', 'fechacreada')
