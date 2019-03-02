from django.db import models

class Comorbilidad(models.Model):

    codcomor = models.AutoField(primary_key=True)
    codenfermedad = models.IntegerField()
    codficha = models.IntegerField()
    fechadiagnostico = models.DateField()

    class Meta:
        ordering = ('codcomor',)