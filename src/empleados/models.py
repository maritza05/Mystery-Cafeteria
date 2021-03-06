from django.db import models
from puestos.models import Puesto

class Empleado(models.Model):
    password = models.CharField(max_length = 25)
    nombre = models.CharField(max_length = 65)
    apellido_paterno = models.CharField('Apellido Paterno', max_length = 120)
    apellido_materno = models.CharField('Apellido Materno', max_length = 120)
    mail = models.EmailField('E-mail', max_length = 60)
    nombre_usuario = models.CharField(max_length = 20)
    puesto = models.ForeignKey(Puesto)


    def __unicode__(self):
        return self.nombre + ' ' + self.apellido_paterno
