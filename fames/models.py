from django.db import models


#models.IntegerField(), models.CharField(max_length=50)

class Fames(models.Model):

    codfame	= models.AutoField(primary_key=True) #código interno único para el fame
    codusuario = models.IntegerField() #	código interno de usuario, para saber quién agrego un fame
    nombre = models.CharField(max_length=50) 	#nombre del fame
    fechacreada = models.DateField(auto_now=True) #	fecha de creación del fame  

    class Meta:
        ordering = ('codfame',)