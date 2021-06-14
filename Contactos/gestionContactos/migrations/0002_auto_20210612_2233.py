# Generated by Django 3.2.4 on 2021-06-13 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionContactos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactos',
            name='apellido',
            field=models.CharField(max_length=50, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='contactos',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo Electronico'),
        ),
        migrations.AlterField(
            model_name='contactos',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='contactos',
            name='numeroCelular',
            field=models.CharField(max_length=11, verbose_name='Teléfono'),
        ),
    ]
