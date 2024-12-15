# meseros/serializers.py
from rest_framework import serializers
from .models import Mesero

class MeseroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesero
        fields = ['id', 'nombre', 'edad', 'procedencia']  # Los campos que queremos exponer
