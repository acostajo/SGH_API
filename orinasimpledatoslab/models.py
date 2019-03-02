from django.db import models

#models.IntegerField(), models.CharField(max_length=50)

class OrinaSimpleDL(models.Model):

    codorinadl = models.AutoField(primary_key=True)
    codorina = models.IntegerField()
    coddatoslab = models.IntegerField()
    

    class Meta:
        ordering = ('codorinadl',)