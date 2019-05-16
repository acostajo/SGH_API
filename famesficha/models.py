from django.db import models
from fames.models import Fames
from ficha.models import Ficha
#models.IntegerField(), models.CharField(max_length=50)

class FamesFicha(models.Model):

    codfameficha = models.AutoField(primary_key=True) #	código interno único para fame asociada a la ficha HA
    codfame = models.IntegerField( )#código interno único para el fame
    codficha = models.IntegerField() #código interno único para la ficha HA, para saber a qué ficha está asociada el fame
    fechadesde = models.DateField(blank=True, null=True) #	fecha desde de consumo del fame
    fechahasta = models.DateField(blank=True, null=True) # fecha hasta de consumo del fame


    class Meta:
        ordering = ('codfameficha',)