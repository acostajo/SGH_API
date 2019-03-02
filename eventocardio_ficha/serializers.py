from rest_framework import serializers
from e.models import EventoCardiovascularFicha  

class EventoCardiovascularFichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoCardiovascularFicha
        fields = ('codevencardofic',
        'codevencardio',
        'codficha')