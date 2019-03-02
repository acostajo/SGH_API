from rest_framework import serializers
from consulta.models import Consulta  

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ('codconsulta',
        'codficha',
        'codusuario',
        'fechaconsulta',
        'diagnostico',
        'evolucion',
        'limitacion',
        'presionarte',
        'frescresp',
        'freccardia',
        'peso',
        'talla',
        'nad',
        'nat',
        'eva',
        'vgp',
        'vgm',
        'cdai',
        'sdai',
        'haq',
        'das28pcr',
        'das28vsg',
        'sientepaci',
        'plan',
        'fechacreada')