from rest_framework import serializers
from famesficha.models import FamesFicha  

class FamesFichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamesFicha
        fields = "__all__"