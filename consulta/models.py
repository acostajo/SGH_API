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
    diagnostico = models.TextField()  # descripción diagnostico
    tratamientoactual = models.TextField(
      blank=True
    )  # descripción tratamiento actual
    evolucion = models.TextField()  # descripción de la evolución
    # descripción de las limitaciones que posee el Paciente
    limitacion = models.TextField()
    limitacionmotivo = models.TextField()
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
    plan = models.TextField(blank=True, null=True)
    # fecha de creación de la consulta
    checkNAD1 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD2 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD3 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD4 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD5 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD6 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD7 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD8 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD9 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD10 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD11 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD12 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD13 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD14 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD15 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD16 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD17 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD18 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD19 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD20 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD21 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD22 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD23 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD24 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD25 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD26 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD27 = models.BooleanField( default=False,blank=True, null=True)
    checkNAD28 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT1 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT2 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT3 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT4 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT5 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT6 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT7 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT8 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT9 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT10 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT11 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT12 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT13 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT14 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT15 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT16 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT17 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT18 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT19 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT20 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT21 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT22 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT23 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT24 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT25 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT26 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT27 = models.BooleanField( default=False,blank=True, null=True)
    checkNAT28 = models.BooleanField( default=False,blank=True, null=True)    

    fechacreada = models.DateField(auto_now=True)

    class Meta:
        ordering = ("-fechaconsulta",)
