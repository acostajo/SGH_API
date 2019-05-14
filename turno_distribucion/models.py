from django.db import models
#models.IntegerField(), models.CharField(max_length=50)

class TurnoDist(models.Model):
    codturnodist=models.AutoField(primary_key=True)
    desturno=models.CharField(null=True,blank=True,max_length=50)
    turno=models.CharField(null=True,blank=True,max_length=50)
    horaturno=models.CharField(null=True,blank=True,max_length=50)

    class Meta:
        ordering = ('codturnodist',)