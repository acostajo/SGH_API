from django.db import models


#models.IntegerField(), models.CharField(max_length=50)

class EventoCardiovascular(models.Model):
    codeventocardio = models.AutoField(primary_key=True) #	código interno único para el evento cardiovascular
    codusuario = models.IntegerField() #	código interno de usuario, para saber quién agrego un evento cardiovascular
    nombre	= models.CharField(max_length=50) #nombre del evento cardiovascular
    fechacreada	= models.DateField(auto_now=True) #fecha de creación del efecto adverso


    class Meta:
        ordering = ('codeventocardio',) 