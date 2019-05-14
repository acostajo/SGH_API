from django.db import models
#models.IntegerField(), models.CharField(max_length=50)

class Turno(models.Model):
    codturno=models.AutoField(primary_key=True)
    codturnodist=models.IntegerField()
    codficha=models.IntegerField()
    codordenestudio=models.IntegerField()
    fechaturno=models.DateField(null=True,blank=True)
    estado=models.CharField(max_length=50)

    class Meta:
        ordering = ('fechaturno',)