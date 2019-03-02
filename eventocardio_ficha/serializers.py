from rest_framework import serializers
from eventocardio_ficha.models import EventoCardiovascularFicha  

class EventoCardiovascularFichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoCardiovascularFicha
        fields = ('codevencardofic',
        'codevencardio',
        'codficha')