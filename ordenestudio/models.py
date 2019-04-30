from django.db import models
from ficha.models import Ficha
from estudio.models import Estudio
# models.IntegerField(), models.CharField(max_length=50)


class OrdenEstudio(models.Model):

    codordenestudio = models.AutoField(primary_key=True)
    codusuario = models.IntegerField(null=True, blank=True)
    codficha = models.ForeignKey(
        Ficha, on_delete=models.DO_NOTHING, null=False, default=0
    )
    codestudio = models.ForeignKey(Estudio,  on_delete=models.DO_NOTHING, null=True )#código interno único para el estudio
    observacion = models.CharField(max_length=200, blank=True)
    estado = models.CharField(max_length=15, blank=True, null=True, default="Pendiente")
    fechaordenestudio = models.DateField(blank=True, null=True)
    fechacreada = models.DateField(auto_now=True)

    class Meta:
        ordering = ("codordenestudio",)
