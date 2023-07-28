from rest_framework import serializers
from locales.models import *

class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = '__all__'  # Include all fields of the model

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'  # Include all fields of the model

class LocalComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalComida
        fields = '__all__'  # Include all fields of the model

class LocalRespuestosSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalRepuestos
        fields = '__all__'  # Include all fields of the model