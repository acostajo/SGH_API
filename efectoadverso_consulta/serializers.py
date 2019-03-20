from rest_framework import serializers
from efectoadverso_consulta.models import EfectoAdversoConsulta


class EfectoAdversoConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EfectoAdversoConsulta
        fields = ('codefecaddl',
                  'codefecad',
                  'codpanolab')
