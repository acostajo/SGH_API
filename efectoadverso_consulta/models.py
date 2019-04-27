from django.db import models


#models.IntegerField(), models.CharField(max_length=50)

class EfectoAdversoConsulta(models.Model):
    # código interno único para el efecto adverso asociado a datos laboratoriales
    codefecaddl = models.AutoField(primary_key=True)
    codefecad = models.IntegerField()  # código interno único para el efecto adverso
    # código interno único para la ficha datos laboratoriales, para saber a qué ficha está asociada los efectos adversos
    codconsulta = models.IntegerField()

    class Meta:
        ordering = ('codefecaddl',)
