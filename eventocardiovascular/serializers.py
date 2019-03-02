from rest_framework import serializers
from eventocardiovascular.models import EventoCardiovascular  

class EventoCardiovascularSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoCardiovascular
        fields = ('codeventocardio',
        'codusuario',
        'nombre',
        'fechacreada')