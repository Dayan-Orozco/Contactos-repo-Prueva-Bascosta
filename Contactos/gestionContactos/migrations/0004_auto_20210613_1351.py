# Generated by Django 3.2.4 on 2021-06-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionContactos', '0003_contactos_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactos',
            name='correo',
            field=models.EmailField(max_length=254, verbose_name='Correo Electronico'),
        ),
        migrations.AlterField(
            model_name='contactos',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='contactos', verbose_name='Foto Contacto'),
        ),
    ]
