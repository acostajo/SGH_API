from django.db import models


#models.IntegerField(), models.CharField(max_length=50)

class EfectoAdversoConsulta(models.Model):
    codefecaddl = models.AutoField(primary_key=True) #	código interno único para el efecto adverso asociado a datos laboratoriales
    codefecad= models.IntegerField() # código interno único para el efecto adverso
    coddatoslab	= models.IntegerField() # código interno único para la ficha datos laboratoriales, para saber a qué ficha está asociada los efectos adversos

    class Meta:
        ordering = ('codefecaddl',)