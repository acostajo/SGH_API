from django.db import models
from ficha.models import Ficha

# models.IntegerField(), models.CharField(max_length=50)


class Consulta(models.Model):
    # código interno único para la ficha consulta
    codconsulta = models.AutoField(primary_key=True)
    # codficha = models.ForeignKey(Ficha, on_delete=models.DO_NOTHING, null=True)
    codficha = models.ForeignKey(
        Ficha, on_delete=models.DO_NOTHING, null=False, default=0)
    # código interno de usuario, para saber quién agrego la ficha de consulta
    codusuario = (models.IntegerField())
    edad = models.IntegerField(default=0)  # edad del paciente
    # fecha en la cual se emitió la consulta
    fechaconsulta = models.DateField(auto_now=True)
    diagnostico = models.CharField(max_length=80)  # descripción diagnostico
    tratamientoactual = models.CharField(
        max_length=200, blank=True)  # descripción tratamiento actual
    evolucion = models.CharField(max_length=80)  # descripción de la evolución
    # descripción de las limitaciones que posee el Paciente
    limitacion = models.CharField(max_length=80)
    limitacionmotivo = models.CharField(max_length=80)
    presionarte = models.IntegerField()  # medida de la presión arterial
    frescresp = models.IntegerField()  # medida de la frecuencia cardíaca
    freccardia = models.IntegerField()  # medida de la frecuencia respiratoria
    peso = models.IntegerField()  # peso
    talla = models.IntegerField()  # talla
    nad = models.IntegerField()  # número de articulaciones dolorosas
    # número de articulaciones tumefactas kore de quien era ese migrate q estaba abierto?, no s, de consulta o de ficha nomas va ser
    nat = models.IntegerField()
    eva = models.IntegerField()  # escala visual analógica
    vgp = models.IntegerField()  # valoración global del Paciente
    vgm = models.IntegerField()  # valoración global del médico
    cdai = models.IntegerField()  # clinical disease activity index
    sdai = models.IntegerField()  # simple disease activity index
    haq = models.IntegerField()  # health assessment questionnaire
    das28pcr = models.IntegerField()  # disease activity score 28 - proteína c reactiva
    # disease activity score 28 - velocidad de sedimentación globular
    das28vsg = (models.IntegerField())
    # escala del 0 (sin dolor) al 10 (máximo dolor)
    sientepaci = models.IntegerField()
    # descripción del plan para el paciente
    plan = models.CharField(max_length=80)
    # fecha de creación de la consulta

    fechacreada = models.DateField(auto_now=True)

    class Meta:
        ordering = ("codconsulta",)
