from rest_framework import serializers
from e.models import EfectoAdverso  

class EfectoAdversoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EfectoAdverso
        fields = ('codefecad',
        'codusuario',
        'nombre',
        'fechacreada')