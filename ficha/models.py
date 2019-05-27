from django.db import models

# models.IntegerField(), models.CharField(max_length=50)


class Ficha(models.Model):
    codpatron = models.IntegerField(
        null=True, blank=True
    )  # código interno único para anapatron, para saber que patron tiene asociada la ficha HA
    codusuario = models.IntegerField(
        null=True, blank=True
    )  # código interno de usuario, para saber quién agrego la ficha
    codficha = models.AutoField(primary_key=True)  # codigo de la ficha
    # nombres completos del paciente
    nombres = models.CharField(max_length=80, blank=True, null=True)
    # apellidos completos del paciente
    apellidos = models.CharField(max_length=80, blank=True, null=True)
    tipodocumento = models.CharField(max_length=30, null=False, default="")
    nrodocumento = models.CharField(
        max_length=10, null=False, unique=True, default=""
    )  # cédula de identidad del paciente
    sexo = models.CharField(max_length=1, blank=True, null=True)  # sexo del paciente
    # fecha de inclusión del paciente
    fechainclusion = models.DateField(blank=True, null=True)
    procedencia = models.CharField(
        max_length=80, blank=True, null=True
    )  # procedencia del paciente
    nacionalidad = models.CharField(
        max_length=80, blank=True, null=True
    )  # nacionalidad del paciente
    escolaridad = models.CharField(
        max_length=80, blank=True, null=True
    )  # escolaridad del paciente
    # diagnóstico inicial del paciente
    diagnostico = models.TextField( blank=True, null=True)
    fechadiagnos = models.DateField(blank=True, null=True)  # fecha del diagnostico
    # fecha de nacimiento del paciente
    fechanaci = models.DateField(blank=True, null=True)
    estadocivil = models.CharField(
        max_length=20, blank=True, null=True
    )  # estado civil del paciente
    profesion = models.CharField(
        max_length=20, blank=True, null=True
    )  # profesión del paciente
    # número de teléfono del paciente
    telefono = models.CharField(max_length=20, blank=True, null=True)
    nhc = models.IntegerField(
        unique=True
    )  # número de historial clínico, código externo de la ficha, por el cual se manejan los usuarios
    iniciosint = models.DateField(
        blank=True, null=True
    )  # Fecha en el que el Paciente empezó a notar síntomas
    formainic = models.TextField(
       blank=True
    )  # Descripción de los síntomas del paciente
    apf = models.TextField(
        blank=True
    )  # Antecedentes Patológicos Familiares
    apfcv = models.TextField(
         blank=True
    )  # Antecedentes patológicos familiares cardiovasculares
    appfractura = models.TextField(
        blank=True
    )  # Antecedentes patológicos personales de fracturas
    apffractura = models.TextField(
     blank=True
    )  # Antecedentes patológicos familiares de fracturas
    protesissitio = models.TextField(
     blank=True
    )  # Datos de prótesis del Paciente
    protefecha = models.DateField(
        null=True, blank=True
    )  # Datos de prótesis del Paciente
    apfneoplasias = models.TextField(
      blank=True
    )  # Antecedentes familiares de neoplasias (tumores)
    sedentarismo = models.BooleanField(null=True)  # Si el Paciente es sedentario
    actifisica = models.BooleanField(
        null=True
    )  # Si el Paciente realiza actividad física
    tabaquismo = models.BooleanField(null=True)  # Si el Paciente es tabaquista
    tabaqfecha = models.DateField(null=True)  # Fecha que comenzo a fumar
    tabnumero =  models.PositiveIntegerField(default=0,null=True)
    extabaq = models.BooleanField(null=True)  # Si fue fumador
    menarca = models.IntegerField(null=True)  # Edad de primera menstruación
    menopausia = models.IntegerField(null=True)  # Edad de menopausia
    edadvidasex = models.IntegerField(null=True, blank=True)
    gestas = models.IntegerField(null=True)  # Cantidad de gestas
    partos = models.IntegerField(null=True)  # Cantidad de partos
    cesareas = models.IntegerField(null=True)  # Cantidad de Cesáreas
    abortos = models.IntegerField(null=True)  # Cantidad de abortos
    hisjospost = models.BooleanField(null=True)  # sí o no, tuvo hijos
    factorreuma_pos = models.CharField(max_length=50, blank=True)  # factor reumatoide
    factorreuma_neg = models.CharField(max_length=50, blank=True)
    factorreuma_nivel = models.CharField(max_length=50, blank=True)
    acpa_pos = models.CharField(max_length=50, blank=True)  # factor reumatoide
    acpa_neg = models.CharField(max_length=50, blank=True)
    acpa_nivel = models.CharField(max_length=50, blank=True)
    ana_pos = models.CharField(max_length=50, blank=True)  # factor reumatoide
    ana_neg = models.CharField(max_length=50, blank=True)
    ana_patron = models.CharField(max_length=50, blank=True)
    rxmanos = models.BooleanField(null=True)  # erecciones sí o no
    rxmanosfecha = models.DateField(null=True)
    rxpies = models.BooleanField(null=True)  # erecciones sí o no
    rxpiesfecha = models.DateField(null=True)
    fechacreadaa = models.DateField(auto_now=True)  # fecha de creación de la ficha HA

    class Meta:
        ordering = ("codficha",)
