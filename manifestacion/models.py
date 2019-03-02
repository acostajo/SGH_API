from django.db import models


#models.IntegerField(), models.CharField(max_length=50)

class Manifestacion(models.Model):
    codmanifficha	= models.AutoField(primary_key=True) #	código interno único para manifestación extra articular asociada a la ficha HA
    codmanif = models.IntegerField() #código interno único para manifestación extra articular
    codficha = models.IntegerField() # código interno de ficha HA, para saber de qué ficha está asociada la manifestación extra articular


    class Meta:
        ordering = ('codmanifficha',)
