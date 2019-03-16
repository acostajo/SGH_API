from rest_framework import serializers
#from ficha.models import Ficha
from ficha.models import Ficha


class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = '__all__'
