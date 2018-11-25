
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Usuario, Mascota

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('user', 'nombre', 'apellido', 'fecha', 'region', 'ciudad', 'vivienda', 'rol')

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ('id', 'nombre', 'raza', 'descripcion', 'estado', 'pic')