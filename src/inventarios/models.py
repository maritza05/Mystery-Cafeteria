from django.db import models
from productos.models import Producto

class Inventario(models.Model):
	id_producto = models.ForeignKey(Producto)
	cantidad = models.IntegerField()