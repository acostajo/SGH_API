from django.db import models
from ficha.models import Ficha

# models.IntegerField(), models.CharField(max_length=50)


class Consulta(models.Model):
    # código interno único para la ficha consulta
    codconsulta = models.AutoField(primary_key=True)
    # codficha = models.ForeignKey(Ficha, on_delete=models.DO_NOTHING, null=True)
    codficha = models.ForeignKey(
        Ficha, on_delete=models.DO_NOTHING, null=False, default=0
    )
    # código interno de usuario, para saber quién agrego la ficha de consulta
    codusuario = models.IntegerField()
    edad = models.IntegerField(default=0)  # edad del paciente
    # fecha en la cual se emitió la consulta
    fechaconsulta = models.DateField()
    diagnostico = models.CharField(max_length=80)  # descripción diagnostico
    tratamientoactual = models.CharField(
        max_length=200, blank=True
    )  # descripción tratamiento actual
    evolucion = models.CharField(max_length=80)  # descripción de la evolución
    # descripción de las limitaciones que posee el Paciente
    limitacion = models.CharField(max_length=80)
    limitacionmotivo = models.CharField(max_length=80)
    presionarte = models.IntegerField(
        blank=True, null=True
    )  # medida de la presión arterial
    frescresp = models.IntegerField(
        blank=True, null=True
    )  # medida de la frecuencia cardíaca
    freccardia = models.IntegerField(
        blank=True, null=True
    )  # medida de la frecuencia respiratoria
    peso = models.DecimalField(
        decimal_places=2, max_digits=5, blank=True, null=True
    )  # peso
    talla = models.DecimalField(
        decimal_places=2, max_digits=5, blank=True, null=True
    )  # talla
    nad = models.IntegerField(
        blank=True, null=True
    )  # número de articulaciones dolorosas
    # número de articulaciones tumefactas kore de quien era ese migrate q estaba abierto?, no s, de consulta o de ficha nomas va ser
    nat = models.IntegerField(blank=True, null=True)
    eva = models.IntegerField(blank=True, null=True)  # escala visual analógica
    vgp = models.IntegerField(blank=True, null=True)  # valoración global del Paciente
    vgp1 = models.IntegerField(blank=True, null=True)  # valoración global del Paciente
    vgp2 = models.IntegerField(blank=True, null=True)  # valoración global del Paciente
    vgm = models.IntegerField(blank=True, null=True)  # valoración global del médico
    vgm1 = models.IntegerField(blank=True, null=True)  # valoración global del médico
    vgm2 = models.IntegerField(blank=True, null=True)  # valoración global del médico
    crp = models.IntegerField(blank=True, null=True)
    vsg = models.IntegerField(blank=True, null=True)
    cdai = models.IntegerField(blank=True, null=True)  # clinical disease activity index
    sdai = models.IntegerField(blank=True, null=True)  # simple disease activity index
    haq = models.IntegerField(blank=True, null=True)  # health assessment questionnaire
    das28pcr = models.DecimalField(
        decimal_places=2, max_digits=5, blank=True, null=True
    )  # disease activity score 28 - proteína c reactiva
    # disease activity score 28 - velocidad de sedimentación globular
    das28vsg = models.DecimalField(
        decimal_places=2, max_digits=5, blank=True, null=True
    )
    # escala del 0 (sin dolor) al 10 (máximo dolor)
    CDAI_RANGO = models.CharField(max_length=80, blank=True, null=True)
    SDAI_RANGO = models.CharField(max_length=80, blank=True, null=True)
    DAS28_VSG_RANGO = models.CharField(max_length=80, blank=True, null=True)
    DAS28_PCR_RANGO = models.CharField(max_length=80, blank=True, null=True)
    sientepaci = models.CharField(max_length=80, blank=True, null=True)
    # descripción del plan para el paciente
    plan = models.CharField(max_length=80, blank=True, null=True)
    # fecha de creación de la consulta

    fechacreada = models.DateField(auto_now=True)

    class Meta:
        ordering = ("-fechaconsulta",)
