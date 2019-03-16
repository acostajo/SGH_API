from django.db import models

# models.IntegerField(), models.CharField(max_length=50)


class Ficha(models.Model):
    codficha = models.AutoField(primary_key=True)  # codigo de la ficha

    # nombres completos del paciente
    nombres = models.CharField(max_length=80, blank=True, null=True)
    # apellidos completos del paciente
    apellidos = models.CharField(max_length=80, blank=True, null=True)
    tipodocumento = models.CharField(max_length=30, null=False, default="")
    nrodocumento = models.CharField(
        max_length=10, null=False, unique=True, default=""
    )  # cédula de identidad del paciente
    sexo = models.CharField(max_length=1, blank=True,
                            null=True)  # sexo del paciente
    # fecha de inclusión del paciente
    fechainclusion = models.DateField(blank=True, null=True)
    procedencia = models.CharField(
        max_length=80, blank=True, null=True)  # procedencia del paciente
    nacionalidad = models.CharField(
        max_length=80, blank=True, null=True)  # nacionalidad del paciente
    escolaridad = models.CharField(
        max_length=80, blank=True, null=True)  # escolaridad del paciente
    # diagnóstico inicial del paciente
    diagnostico = models.CharField(max_length=80, blank=True, null=True)
    fechadiagnos = models.DateField(
        blank=True, null=True)  # fecha del diagnostico
    # fecha de nacimiento del paciente
    fechanaci = models.DateField(blank=True, null=True)
    estadocivil = models.CharField(
        max_length=20, blank=True, null=True
    )  # estado civil del paciente
    profesion = models.CharField(
        max_length=20, blank=True, null=True)  # profesión del paciente
    # número de teléfono del paciente
    telefono = models.CharField(max_length=20, blank=True, null=True)
    codpatron = models.IntegerField(
        null=True, blank=True
    )  # código interno único para anapatron, para saber que patron tiene asociada la ficha HA
    codusuario = models.IntegerField(
        null=True, blank=True
    )  # código interno de usuario, para saber quién agrego la ficha
    nhc = models.IntegerField(
        unique=True
    )  # número de historial clínico, código externo de la ficha, por el cual se manejan los usuarios
    iniciosint = models.DateField(
        blank=True, null=True
    )  # Fecha en el que el Paciente empezó a notar síntomas
    formainic = models.CharField(
        max_length=50, blank=True
    )  # Descripción de los síntomas del paciente
    apf = models.CharField(
        max_length=50, blank=True
    )  # Antecedentes Patológicos Familiares
    apfcv = models.CharField(
        max_length=50, blank=True
    )  # Antecedentes patológicos familiares cardiovasculares
    appfractura = models.CharField(
        max_length=50, blank=True
    )  # Antecedentes patológicos personales de fracturas
    apffractura = models.CharField(
        max_length=50, blank=True
    )  # Antecedentes patológicos familiares de fracturas
    protesissitio = models.CharField(
        max_length=50, blank=True
    )  # Datos de prótesis del Paciente
    protefecha = models.DateField(
        null=True, blank=True
    )  # Datos de prótesis del Paciente
    apfneoplasias = models.CharField(
        max_length=50, blank=True
    )  # Antecedentes familiares de neoplasias (tumores)
    sedentarismo = models.BooleanField()  # Si el Paciente es sedentario
    actifisica = models.BooleanField()  # Si el Paciente realiza actividad física
    # tabaquismo = models.BooleanField(null=True)  # Si el Paciente es tabaquista
    # Fecha que comenzo a fumar
    tabaqfecha = models.DateField(blank=True, null=True)
    tabnumero = models.IntegerField(null=True, blank=True)
    extabaq = models.BooleanField()  # Si fue fumador
    menarca = models.IntegerField()  # Edad de primera menstruación
    menopausia = models.IntegerField()  # Edad de menopausia
    edadvidasex = models.IntegerField(null=True, blank=True)
    gestas = models.IntegerField()  # Cantidad de gestas
    partos = models.IntegerField()  # Cantidad de partos
    cesareas = models.IntegerField()  # Cantidad de Cesáreas
    abortos = models.IntegerField()  # Cantidad de abortos
    hisjospost = models.BooleanField()  # sí o no, tuvo hijos
    factorreuma_pos = models.CharField(
        max_length=50, blank=True)  # factor reumatoide
    factorreuma_neg = models.CharField(max_length=50, blank=True)
    factorreuma_nivel = models.CharField(max_length=50, blank=True)
    acp_pos = models.CharField(max_length=50, blank=True)  # factor reumatoide
    acp_neg = models.CharField(max_length=50, blank=True)
    acp_nivel = models.CharField(max_length=50, blank=True)
    ana_pos = models.CharField(max_length=50, blank=True)  # factor reumatoide
    ana_neg = models.CharField(max_length=50, blank=True)
    ana_patron = models.CharField(max_length=50, blank=True)
    rxmanos = models.BooleanField()  # erecciones sí o no
    rxmanosfecha = models.DateField(blank=True, null=True)
    rxpies = models.BooleanField()  # erecciones sí o no
    rxpiesfecha = models.DateField(blank=True, null=True)
    # fecha de creación de la ficha HA
    fechacreadaa = models.DateField(auto_now=True)

    class Meta:
        ordering = ("codficha",)
