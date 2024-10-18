from rest_framework import serializers
from .models import CustomUserModel

class CustomUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = '__all__'
