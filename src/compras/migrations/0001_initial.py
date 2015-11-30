# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
        ('inventarios', '0001_initial'),
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('monto', models.IntegerField()),
                ('id_empleado', models.ForeignKey(to='empleados.Empleado')),
                ('id_inventario', models.ForeignKey(to='inventarios.Inventario')),
                ('id_proveedor', models.ForeignKey(to='proveedores.Proveedor')),
            ],
        ),
    ]
