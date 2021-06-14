from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH


# Create your models here.

#AQUI GESTIONAMOS LOS CONTACTOS
class Contactos(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellidos")
    numeroCelular = models.CharField(max_length=11 , verbose_name="Número de Celular")
    foto = models.ImageField(blank=True, null=True, upload_to="contactos", verbose_name="Foto Contacto")
    correo = models.EmailField(verbose_name="Correo Electronico")
    
    def __str__(self):
        return self.nombre
        #return "El Correo es: %s De %s y su Telefono es: %s" %(self.correo, self.nombre, self.numeroCelular)
        
