# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puestos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=25)),
                ('nombre', models.CharField(max_length=65)),
                ('apellido_paterno', models.CharField(max_length=120, verbose_name=b'Apellido Paterno')),
                ('apellido_materno', models.CharField(max_length=120, verbose_name=b'Apellido Materno')),
                ('mail', models.EmailField(max_length=60, verbose_name=b'E-mail')),
                ('nombre_usuario', models.CharField(max_length=20)),
                ('puesto', models.ForeignKey(to='puestos.Puesto')),
            ],
        ),
    ]
