from django.db import models
from django.utils import timezone
class Archivo(models.Model):
    archivo_id = models.AutoField(primary_key=True)
    archivo = models.FileField(null=True, max_length=255)
    codordenestudio = models.IntegerField(null=True, blank=True)
    fecha_creada = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.archivo.name)