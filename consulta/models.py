from django.db import models
from ficha.models import Ficha

#models.IntegerField(), models.CharField(max_length=50)

class Consulta(models.Model):
    codconsulta	= models.AutoField(primary_key=True) #código interno único para la ficha consulta
    codficha = models.ManyToManyField(Ficha, blank=False, null=True)
    #codficha = models.ForeignKey(Ficha, on_delete=models.DO_NOTHING, null=True)
    codusuario = models.IntegerField() #código interno de usuario, para saber quién agrego la ficha de consulta
    edad = models.IntegerField(default=0) #edad del paciente
    fechaconsulta = models.DateField(auto_now=True) #fecha en la cual se emitió la consulta
    diagnostico = models.CharField(max_length=80) #descripción diagnostico
    evolucion= models.CharField(max_length=80) #descripción de la evolución
    limitacion = models.CharField(max_length=80) #descripción de las limitaciones que posee el Paciente
    presionarte = models.IntegerField() #medida de la presión arterial
    frescresp = models.IntegerField() #	medida de la frecuencia cardíaca
    freccardia = models.IntegerField() #medida de la frecuencia respiratoria
    peso = models.IntegerField() #peso
    talla = models.IntegerField() #talla
    nad = models.IntegerField() #número de articulaciones dolorosas
    nat = models.IntegerField() #número de articulaciones tumefactas
    eva	= models.IntegerField() #escala visual analógica
    vgp	= models.IntegerField() #valoración global del Paciente
    vgm	= models.IntegerField() #valoración global del médico
    cdai = models.IntegerField() #clinical disease activity index
    sdai = models.IntegerField() #simple disease activity index
    haq = models.IntegerField() #health assessment questionnaire
    das28pcr = models.IntegerField() #disease activity score 28 - proteína c reactiva
    das28vsg = models.IntegerField() #disease activity score 28 - velocidad de sedimentación globular
    sientepaci = models.IntegerField() #escala del 0 (sin dolor) al 10 (máximo dolor)
    plan = models.CharField(max_length=80) #descripción del plan para el paciente
    fechacreada = models.DateField(auto_now=True) #fecha de creación de la consulta

    class Meta:
        ordering = ('codconsulta',)