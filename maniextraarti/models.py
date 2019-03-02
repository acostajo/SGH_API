from django.db import models


#models.IntegerField(), models.CharField(max_length=50)

class ManiExtraArti(models.Model):

   codmanif = models.AutoField(primary_key=True) #	código interno único para manifestación extra articular
   codusuario = models.IntegerField() #	código interno de usuario, para saber quién agrego una manifestación extra articular
   nombre = models.CharField(max_length=50) 	#nombre de la manifestación extra articular
   descripcion	= models.CharField(max_length=50) 	#descripción de la manifestación extra articular
   fechacreada	= models.DateField(auto_now=True) #	fecha de creación de la manifestación extra articular


   class Meta:
      ordering = ('codmanif',)