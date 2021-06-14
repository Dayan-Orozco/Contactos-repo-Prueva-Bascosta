from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from gestionContactos.models import Contactos

# Register your models here.
class ContactosAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellido", "numeroCelular", "correo", "foto")
    search_fields=("nombre", "numeroCelular")
    list_per_page = 20

admin.site.register(Contactos, ContactosAdmin)