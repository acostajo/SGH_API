from django.db import models

#models.IntegerField(), models.CharField(max_length=50)

class OrinaSimple(models.Model):

    codorina = models.AutoField(primary_key=True)
    codusuario = models.IntegerField()
    nombre = models.CharField(max_length=50)
    fechacreada = models.DateField()

    class Meta:
        ordering = ('codorina',)