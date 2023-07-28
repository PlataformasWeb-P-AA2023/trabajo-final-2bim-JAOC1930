from rest_framework import serializers
from locales.models import *

class BarrioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Barrio
        fields = '__all__'  # Include all fields of the model

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'  # Include all fields of the model

class LocalComidaSerializer(serializers.HyperlinkedModelSerializer):
    barrio_str = serializers.StringRelatedField(source="barrio", read_only=True)
    propietario_str = serializers.StringRelatedField(source="propietario", read_only=True)
    class Meta:
        model = LocalComida
        fields = '__all__'  # Include all fields of the model

class LocalRespuestosSerializer(serializers.HyperlinkedModelSerializer):
    barrio_str = serializers.StringRelatedField(source="barrio", read_only=True)
    propietario_str = serializers.StringRelatedField(source="propietario", read_only=True)
    class Meta:
        model = LocalRepuestos
        fields = '__all__'  # Include all fields of the model