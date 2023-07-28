from django.contrib import admin
from locales.models import *
# Register your models here.

class BarrioAdmin(admin.ModelAdmin):
    model = Barrio
    list_display = ['nombre']
    list_filter = ['nombre']

admin.site.register(Barrio, BarrioAdmin)

class PersonaAdmin(admin.ModelAdmin):
    model = Persona
    list_display = ['nombre', 'apellido', 'cedula']
    list_filter = ['nombre', 'apellido', 'cedula']

admin.site.register(Persona, PersonaAdmin)

class LocalComidaAmdin(admin.ModelAdmin):
    model = LocalComida
    list_display = ['propietario', 'direccion', 'barrio', 'tipo_comida', 'ventas_proyectadas_mes']
    list_filter = ['propietario', 'direccion', 'barrio', 'tipo_comida', 'ventas_proyectadas_mes']

admin.site.register(LocalComida, LocalComidaAmdin)

class LocalRespuestosAdmin(admin.ModelAdmin):
    model = LocalRepuestos
    list_display = ['propietario', 'direccion', 'barrio', 'valor_total_mercaderia']
    list_filter = ['propietario', 'direccion', 'barrio', 'valor_total_mercaderia']

admin.site.register(LocalRepuestos, LocalRespuestosAdmin)