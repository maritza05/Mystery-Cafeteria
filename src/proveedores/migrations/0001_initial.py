# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organizacion', models.CharField(max_length=65)),
                ('email', models.EmailField(max_length=254)),
                ('numero_telefono', models.CharField(max_length=10)),
            ],
        ),
    ]
