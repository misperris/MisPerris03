
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('user', 'nombre', 'apellido', 'fecha', 'region', 'ciudad', 'vivienda', 'rol')

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ('id', 'nombre', 'raza', 'descripcion', 'estado', 'pic')