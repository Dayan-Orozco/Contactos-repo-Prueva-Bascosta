from typing import Container
import django
from django.http import HttpRequest, response
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from gestionContactos.forms import formularioRegContacto
from gestionContactos.models import Contactos 


def home(request):
    return render(request, "home.html")

def contactos(request):

    contactos = Contactos.objects.all()
    data={
        "contactos": contactos
    }
    return render(request, "contactos.html", data)
    
def registrar(request):
    
    if request.method == 'POST':

        form = formularioRegContacto(request.POST, request.FILES)
        #si el fomrulario es valido lo insertamos enn la bd
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'registro.html', {'form': form, 'img_obj': img_obj})
    else:
        form = formularioRegContacto()
    return render(request, 'registro.html', {'form': form})

def editar(request, id_con):
    contactos = Contactos.objects.get(id = id_con)

    if request.method == 'POST':
        form = formularioRegContacto(request.POST, request.FILES, instance=contactos)
        if form.is_valid():
            form.save()
            return redirect(to="Contactos")
    else:
        form = formularioRegContacto(instance=contactos)
       
    context = {'form': form}
    return render(request, "editar.html", context)

def eliminar(request, id_con):
    contacto = Contactos.objects.get(id = id_con)
    contacto.delete()
    return redirect(to="Contactos")