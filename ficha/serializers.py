from rest_framework import serializers
#from ficha.models import Ficha  
from ficha.models import Ficha, Paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('codpaciente',
        'codusuario',
        'nombres',
        'apellidos',
        'cedula',
        'sexo',
        'fechainclusion',
        'procedencia',
        'nacionalidad',
        'escolaridad',
        'diagnostico',
        'fechadiagnos',
        'fechanaci',
        'estadocivil',
        'profesion',
        'telefono',
        'lineabaja',
        'fechacreada')


class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = ('codficha',
        'codpaciente',
        'codpatron',
        'codusuario',
        'nhc',
        'iniciosint',
        'formainic',
        'apf',
        'apfcv',
        'appfractura',
        'apffractura',
        'protesissitio',
        'protefecha',
        'apfneoplasias',
        'sedentarismo',
        'actifisica',
        'tabaqfecha',
        'tabnumero',
        'extabaq',
        'menarca',
        'menopausia',
        'edadvidasex',
        'gestas',
        'partos',
        'cesareas',
        'abortos',
        'hisjospost',
        'factorreuma',
        'acp',
        'acp_nivel',
        'rxmanos',
        'rxmanosfecha',
        'rxpies',
        'rxpiesfecha',
        'fechacreadaa')

