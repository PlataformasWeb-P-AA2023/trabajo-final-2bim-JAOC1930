from django import forms
from locales.models import *

class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre']

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'cedula']

class LocalComidaForm(forms.ModelForm):
    class Meta:
        model = LocalComida
        fields = ['propietario', 'direccion', 'barrio', 'tipo_comida', 'ventas_proyectadas_mes']

class LocalRespuestosForm(forms.ModelForm):
    class Meta:
        model = LocalRepuestos
        fields = ['propietario', 'direccion', 'barrio', 'valor_total_mercaderia']

