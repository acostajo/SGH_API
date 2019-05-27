from django.db import models
from ficha.models import Ficha

# models.IntegerField(), models.CharField(max_length=50)


class Panolab(models.Model):
    # código interno único para la ficha panorámica de laboratorio
    codpanolab = models.AutoField(primary_key=True)
    fechapanolab = models.DateField(null=True, blank=True)
    # código interno único para la ficha HA, para saber a qué ficha HA está asociada la ficha panorámica de laboratorio
    codficha = models.ForeignKey(Ficha, on_delete=models.DO_NOTHING, null=False)
    # código interno de usuario, para saber quién agrego la ficha panorámica de laboratorio
    codusuario = models.IntegerField(null=True, blank=True)
    # el paciente tiene prótesis, sí o no
    fechapanolab = models.DateField(blank=True, null=True)
    protesis = models.CharField(max_length=2, blank=True)
    hemoglobina = models.IntegerField(blank=True, null=True)  # cantidad hemoglobina
    hemotocrito = models.IntegerField(blank=True, null=True)  # cantidad hematocrito
    # cantidad de volumen corpuscular medio
    vcm = models.IntegerField(blank=True, null=True)
    # cantidad de glóbulos blancos
    globlanco = models.IntegerField(blank=True, null=True)
    # cantidad de neutrófilos/linfocitos
    nl = models.IntegerField(blank=True, null=True)
    plaqueta = models.IntegerField(blank=True, null=True)  # cantidad de plaquetas
    # transaminasa glutámico-oxalacética desde
    gotdesde = models.IntegerField(blank=True, null=True)
    # transaminasa glutámico-oxalacética hasta
    gothasta = models.IntegerField(blank=True, null=True)
    # transaminasa glutámico-pirúvica desde
    gptdesde = models.IntegerField(blank=True, null=True)
    # transaminasa glutámico-pirúvica hasta
    gpthasta = models.IntegerField(blank=True, null=True)
    # cantidad total de bilirrubina
    bilirrubina = models.IntegerField(blank=True, null=True)
    uresa = models.IntegerField(blank=True, null=True)  # cantidad de urea
    # velocidad de sedimentación globular
    vsg = models.IntegerField(blank=True, null=True)
    # cantidad de proteína c reactiva
    pcr = models.IntegerField(blank=True, null=True)
    glicemia = models.IntegerField(blank=True, null=True)  # cantidad de glicemia
    # cantidad total de colesterol
    coleste = models.IntegerField(blank=True, null=True)
    ldl = models.IntegerField(blank=True, null=True)  # low density lipoprotein
    # high density lipoprotein
    hdl = models.IntegerField(blank=True, null=True)
    # very low density lipoprotein
    vldl = models.IntegerField(blank=True, null=True)
    trigliceri = models.IntegerField(blank=True, null=True)  # cantidad de triglicéridos
    acidourico = models.IntegerField(blank=True, null=True)  # cantidad de ácido úrico
    frdesde = models.IntegerField(blank=True, null=True)  # factor reumatoide desde
    frhasta = models.IntegerField(blank=True, null=True)  # factor reumatoide hasta
    # cantidad de anticuerpo anti péptido citrulinado cíclico negativo
    anticcpneg = models.IntegerField(blank=True, null=True)
    # cantidad de anticuerpo anti péptido citrulinado cíclico positivo
    anticcppost = models.IntegerField(blank=True, null=True)
    # descripción para el anticcppost
    anticcpposd = models.CharField(max_length=80, blank=True, null=True)
    # cantidad de anticuerpo anti nuclear positivo
    anaposit = models.IntegerField(blank=True, null=True)
    # cantidad de anticuerpo anti nuclear negativo
    ananeg = models.IntegerField(blank=True, null=True)
    # cantidad de anticuerpo anti DNA positivo
    antidnapos = models.IntegerField(blank=True, null=True)
    # cantidad de anticuerpo anti DNA negativo
    antidnaneg = models.IntegerField(blank=True, null=True)
    prot24 = models.IntegerField(blank=True, null=True)  # proteinuria de 24hs
    # información adicional que se puede incluir
    observacion = models.TextField(blank=True, null=True)
    # fecha de creación de la orden de medicamento
    fechacreada = models.DateField(auto_now=True)

    class Meta:
        ordering = ("-fechapanolab",)
