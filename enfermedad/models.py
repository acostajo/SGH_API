from django.db import models

#models.IntegerField(), models.CharField(max_length=50)

class Enfermedad(models.Model):

    codenfermedad = models.AutoField(primary_key=True)
    codusuario = models.IntegerField(null = True)
    nombre = models.CharField(max_length=50)
    fechacreada = models.DateField(auto_now=True)

    class Meta:
        ordering = ('codenfermedad',)