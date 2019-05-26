from django.db import models

#models.IntegerField(), models.CharField(max_length=50)

class Agenda(models.Model):

    codagenda = models.AutoField(primary_key=True)
    codusuario = models.IntegerField(null = True)
    nombres = models.TextField()
    apellidos = models.TextField()
    orden=models.IntegerField(null = True)
    estado=models.IntegerField(null = True, default=0)
    fechacreada = models.DateField(auto_now=True)

    class Meta:
        ordering = ('codagenda',)
