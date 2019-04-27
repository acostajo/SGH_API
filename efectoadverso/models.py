from django.db import models


#models.IntegerField(), models.CharField(max_length=50)

class EfectoAdverso(models.Model):
    codefecad = models.AutoField(primary_key=True) #código interno único para el efecto adverso
    codusuario = models.IntegerField(null=True) #código interno de usuario, para saber quién agrego un efecto adverso
    nombre =  models.CharField(max_length=50)	#nombre del efecto adverso
    fechacreada = models.DateField(auto_now=True) #fecha de creación del efecto adverso

    class Meta:
        ordering = ('codefecad',)