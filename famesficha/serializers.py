from rest_framework import serializers
from e.models import FamesFicha  

class FamesFichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamesFicha
        fields = ('codfameficha',
        'codfame',
        'codficha',
        'fechadesde',
        'fechahasta')