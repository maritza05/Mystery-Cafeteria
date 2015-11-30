from django.db import models

class Producto(models.Model):
	nombre = models.CharField('Nombre', max_length = 120)
	descripcion = models.CharField('Descripcion', max_length = 120)
	precio = models.DecimalField(max_digits=20, decimal_places=3)

