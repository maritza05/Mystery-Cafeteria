# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120, verbose_name=b'Nombre')),
                ('descripcion', models.CharField(max_length=120, verbose_name=b'Descripcion')),
                ('precio', models.DecimalField(max_digits=20, decimal_places=3)),
            ],
        ),
    ]
