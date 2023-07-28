from django.shortcuts import render, redirect
from locales.models import *
from locales.form import *
from rest_framework import viewsets, permissions
from .serializers import *
# Create your views here.
def index(request):
    barrio = Barrio.objects.all()
    persona = Persona.objects.all()
    localComida = LocalComida.objects.all()
    localRepuestos = LocalRepuestos.objects.all()
    num_localComida = len(localComida)
    diccionario = {'num_locaComida': num_localComida, 'localComida': localComida}
    return render(request, 'index.html', diccionario)

##################################################################################


def crear_Barrio(request):
    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() 
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearBarrio.html', diccionario)

def editar_Barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)

def eliminar_Barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    barrio.delete()
    return redirect(index)

##################################################################################

def crear_Persona(request):
    if request.method=='POST':
        formulario = PersonaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() 
            return redirect(index)
    else:
        formulario = PersonaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearPersona.html', diccionario)

def editar_Persona(request, id):
    persona = Persona.objects.get(pk=id)
    if request.method=='POST':
        formulario = PersonaForm(request.POST, instance=persona)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = PersonaForm(instance=persona)
    diccionario = {'formulario': formulario}

    return render(request, 'editarPersona.html', diccionario)

def eliminar_Persona(request, id):
    persona = Persona.objects.get(pk=id)
    persona.delete()
    return redirect(index)

##################################################################################

def crear_LocalComida(request):
    if request.method=='POST':
        formulario = LocalComidaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() 
            return redirect(index)
    else:
        formulario = LocalComidaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearLocalComida.html', diccionario)

def editar_LocalComida(request, id):
    localComida = LocalComida.objects.get(pk=id)
    if request.method=='POST':
        formulario = LocalComidaForm(request.POST, instance=localComida)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = LocalComidaForm(instance=localComida)
    diccionario = {'formulario': formulario}

    return render(request, 'editarLocalComida.html', diccionario)

def eliminar_LocalComida(request, id):
    localComida = LocalComida.objects.get(pk=id)
    localComida.delete()
    return redirect(index)

##################################################################################

def crear_LocalRespuestos(request):
    if request.method=='POST':
        formulario = LocalRespuestosForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() 
            return redirect(index)
    else:
        formulario = LocalRespuestosForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearLocalRespuestos.html', diccionario)

def editar_LocalRespuestos(request, id):
    localRespuestos = LocalRespuestosForm.objects.get(pk=id)
    if request.method=='POST':
        formulario = LocalRespuestosForm(request.POST, instance=localRespuestos)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = LocalRespuestosForm(instance=localRespuestos)
    diccionario = {'formulario': formulario}

    return render(request, 'editarLocalRespuestos.html', diccionario)

def eliminar_LocalRespuestos(request, id):
    localRespuestos = LocalRepuestos.objects.get(pk=id)
    localRespuestos.delete()
    return redirect(index)

########################################################################33

class BarrioViewSet(viewsets.ModelViewSet):
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAuthenticated]

class LocalComidaViewSet(viewsets.ModelViewSet):
    queryset = LocalComida.objects.all()
    serializer_class = LocalComidaSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocalRespuestosViewSet(viewsets.ModelViewSet):
    queryset = LocalRepuestos.objects.all()
    serializer_class = LocalRespuestosSerializer
    permission_classes = [permissions.IsAuthenticated]