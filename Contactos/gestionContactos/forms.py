from django import forms
from django.core.exceptions import ValidationError
from gestionContactos.models import Contactos


class formularioRegContacto(forms.ModelForm):
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class":"form-control"}))
    apellido = forms.CharField(label="Apellidos", widget=forms.TextInput(attrs={"class":"form-control"}))
    correo = forms.EmailField(max_length=250, label="Correo Electronico", widget=forms.EmailInput(attrs={"class":"form-control"}))
    numeroCelular = forms.CharField(label="Número de Celular", widget=forms.TextInput(attrs={"class":"form-control"})) 
    foto = forms.ImageField(label="Subir Foto", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))

    #con este bloque validamoas si un numero ya existe
    def clean_numeroCelular(self):
        numeroCelular = self.cleaned_data['numeroCelular']
        existe = Contactos.objects.filter(numeroCelular = numeroCelular).exists()
        if existe:
            raise ValidationError('Este número de Celular ya Existe')
        return numeroCelular



    class Meta:
        model = Contactos
        fields = ('nombre', 'apellido', 'correo', 'numeroCelular', 'foto')
        #fields = "__all__"