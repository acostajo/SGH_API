from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User


class CustomRegisterSerializer(RegisterSerializer):

    username = serializers.CharField(required=True)
    tipo = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'username': self.validated_data.get('username', ''),
            'tipo': self.validated_data.get('tipo', ''),
        }

class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
       