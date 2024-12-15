from rest_framework import serializers
from .models import Plato  # Asegúrate de que este modelo exista

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'  # Serializa todos los campos del modelo
