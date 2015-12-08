#coding: utf-8
from django import forms
from empleados.models import Empleado


class EmpleadoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label=u'Contraseña')

    class Meta(object):
        model = Empleado
        fields = ['nombre', 'password', 'apellido_paterno', 'apellido_materno', 'mail', 'nombre_usuario', 'puesto']
