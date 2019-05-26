from django.db import models
from ficha.models import Ficha
from estudio.models import Estudio

# models.IntegerField(), models.CharField(max_length=50)


class OrdenEstudio(models.Model):

    codordenestudio = models.AutoField(primary_key=True)
    codusuario = models.IntegerField(null=True, blank=True)
    codficha = models.IntegerField(null=True, blank=True)
    codestudio = models.IntegerField(null=True, blank=True) 
    observacion = models.CharField(max_length=200, blank=True)
    estado = models.CharField(max_length=15, blank=True, null=True, default="Pendiente")
    fechaordenestudio = models.DateField(blank=True, null=True)
    fechacreada = models.DateField(auto_now=True)

    class Meta:
        ordering = ("-fechaordenestudio",)
