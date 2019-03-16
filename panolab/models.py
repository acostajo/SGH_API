from django.db import models
from ficha.models import Ficha

# models.IntegerField(), models.CharField(max_length=50)


class Panolab(models.Model):
    # código interno único para la ficha panorámica de laboratorio
    coddatoslab = models.AutoField(primary_key=True)
    # código interno único para la ficha HA, para saber a qué ficha HA está asociada la ficha panorámica de laboratorio
    codficha = models.ForeignKey(
        Ficha, on_delete=models.DO_NOTHING, null=False, default=0)
    # código interno de usuario, para saber quién agrego la ficha panorámica de laboratorio
    codusuario = (models.IntegerField())
    # el paciente tiene prótesis, sí o no
    protesis = models.CharField(max_length=2)
    hemoglobina = models.IntegerField()  # cantidad hemoglobina
    hemotocrito = models.IntegerField()  # cantidad hematocrito
    vcm = models.IntegerField()  # cantidad de volumen corpuscular medio
    globlanco = models.IntegerField()  # cantidad de glóbulos blancos
    nl = models.IntegerField()  # cantidad de neutrófilos/linfocitos
    plaqueta = models.IntegerField()  # cantidad de plaquetas
    gotdesde = models.IntegerField()  # transaminasa glutámico-oxalacética desde
    gothasta = models.IntegerField()  # transaminasa glutámico-oxalacética hasta
    gptdesde = models.IntegerField()  # transaminasa glutámico-pirúvica desde
    gpthasta = models.IntegerField()  # transaminasa glutámico-pirúvica hasta
    bilirrubina = models.IntegerField()  # cantidad total de bilirrubina
    uresa = models.IntegerField()  # cantidad de urea
    vsg = models.IntegerField()  # velocidad de sedimentación globular
    pcr = models.IntegerField()  # cantidad de proteína c reactiva
    glicemia = models.IntegerField()  # cantidad de glicemia
    coleste = models.IntegerField()  # cantidad total de colesterol
    ldl = models.IntegerField()  # low density lipoprotein
    hdl = models.IntegerField()  # high density lipoprotein
    vldl = models.IntegerField()  # very low density lipoprotein
    trigliceri = models.IntegerField()  # cantidad de triglicéridos
    acidourico = models.IntegerField()  # cantidad de ácido úrico
    frdesde = models.IntegerField()  # factor reumatoide desde
    frhasta = models.IntegerField()  # factor reumatoide hasta
    # cantidad de anticuerpo anti péptido citrulinado cíclico negativo
    anticcpneg = models.IntegerField()
    # cantidad de anticuerpo anti péptido citrulinado cíclico positivo
    anticcppost = models.IntegerField()
    # descripción para el anticcppost
    anticcpposd = models.CharField(max_length=80)
    anaposit = models.IntegerField()  # cantidad de anticuerpo anti nuclear positivo
    ananeg = models.IntegerField()  # cantidad de anticuerpo anti nuclear negativo
    antidnapos = models.IntegerField()  # cantidad de anticuerpo anti DNA positivo
    antidnaneg = models.IntegerField()  # cantidad de anticuerpo anti DNA negativo
    prot24 = models.IntegerField()  # proteinuria de 24hs
    # información adicional que se puede incluir
    observacion = models.CharField(max_length=80)
    # fecha de creación de la orden de medicamento
    fechacreada = models.DateField(auto_now=True)

    class Meta:
        ordering = ("coddatoslab",)
