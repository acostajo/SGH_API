from rest_framework import serializers
from comorbilidades.models import Comorbilidad

class ComorbilidadSerializer(serializers.ModelSerializer):
    """Orina simple class."""
    class Meta:
        model = Comorbilidad
        fields = ('codcomor', 'codenfermedad', 'codficha', 'fechadiagnostico')
