from django.db import models


class Archivo(models.Model):
    archivo = models.FileField(blank=False, null=False)
    codordenestudio = models.IntegerField(null=True, blank=True)
    fechacreada = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.archivo.name  