from django.db import models
from eventocardiovascular.models import EventoCardiovascular
from ficha.models import Ficha

#models.IntegerField(), models.CharField(max_length=50)

class EventoCardiovascularFicha(models.Model):
    codevencardofic = models.AutoField(primary_key=True) #código interno único para el evento cardiovascular asociado a la ficha
    codeventocardio = models.IntegerField() # código interno único para el evento cardiovascular
    #codficha	= models.IntegerField() # código interno único para la ficha HA, para saber a qué ficha HA está asociada el evento cardiovascular
    codficha	= models.IntegerField() # código interno único para la ficha HA, para saber a qué ficha HA está asociada el evento cardiovascular 

    class Meta:
        ordering = ('codevencardofic',)

        