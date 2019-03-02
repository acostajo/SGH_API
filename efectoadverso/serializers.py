from rest_framework import serializers
from efectoadverso.models import EfectoAdverso  

class EfectoAdversoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EfectoAdverso
        fields = ('codefecad',
        'codusuario',
        'nombre',
        'fechacreada')