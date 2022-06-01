from dataclasses import fields
from .models import Menu
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
    
    def create(self,validated_data):
        return Menu.objects.create(**validated_data)