from django.db import models


#models.IntegerField(), models.CharField(max_length=50)

class Ficha(models.Model):
    codficha = models.AutoField(primary_key=True) #codigo de la ficha
    codpaciente = models.IntegerField() #codigo del paciente 
    codpatron = models.IntegerField() #código interno único para anapatron, para saber que patron tiene asociada la ficha HA
    codusuario = models.IntegerField() #código interno de usuario, para saber quién agrego la ficha
    nhc = models.IntegerField() #número de historial clínico, código externo de la ficha, por el cual se manejan los usuarios
    iniciosint = models.DateField() #Fecha en el que el Paciente empezó a notar síntomas
    formainic = models.CharField(max_length=50)	#Descripción de los síntomas del paciente
    apf	= models.CharField(max_length=50) #Antecedentes Patológicos Familiares
    apfcv = models.CharField(max_length=50) #Antecedentes patológicos familiares cardiovasculares
    appfractura = models.CharField(max_length=50) #Antecedentes patológicos personales de fracturas
    apffractura	= models.CharField(max_length=50) #Antecedentes patológicos familiares de fracturas
    protesissitio = models.CharField(max_length=50) #Datos de prótesis del Paciente
    protefecha = models.DateField() #Datos de prótesis del Paciente
    apfneoplasias = models.IntegerField() #Antecedentes familiares de neoplasias (tumores)
    sedentarismo = models.BooleanField() #Si el Paciente es sedentario
    actifisica = models.BooleanField() #Si el Paciente realiza actividad física
    tabaqfecha = models.DateField() #Fecha que comenzo a fumar
    tabnumero  = models.IntegerField() #Número  de paquetes que fuma/fumo por dia 
    extabaq = models.BooleanField() #Si fue fumador
    menarca = models.IntegerField() #Edad de primera menstruación
    menopausia = models.IntegerField() #Edad de menopausia
    edadvidasex	= models.IntegerField()#A los cuantos años comenzó a tener actividad sexual
    gestas = models.IntegerField() #Cantidad de gestas
    partos = models.IntegerField() #Cantidad de partos
    cesareas = models.IntegerField() #Cantidad de Cesáreas
    abortos = models.IntegerField() #Cantidad de abortos
    hisjospost = models.BooleanField() #sí o no, tuvo hijos
    factorreuma = models.IntegerField() #factor reumatoide
    acp = models.IntegerField() #anticuerpos antipéptidos cíclicos citrulinados
    acp_nivel = models.IntegerField() #anticuerpo antinuclear
    rxmanos = models.BooleanField() #erecciones sí o no
    rxmanosfecha = models.DateField() #la fecha que tuvo las erecciones ----------> wtf erecciones hei
    rxpies = models.BooleanField() #erecciones sí o no
    rxpiesfecha = models.DateField() #la fecha que tuvo las erecciones
    fechacreadaa = models.DateField(auto_now=True)#fecha de creación de la ficha HA

    class Meta:
        ordering = ('codficha',)