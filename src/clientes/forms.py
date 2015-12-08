#coding: utf-8
from django import forms
from clientes.models import Cliente


class ClientesForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label=u'Contraseña')

    class Meta(object):
        model = Cliente
        fields = ['nombre', 'password', 'apellido_paterno', 'apellido_materno', 'mail', 'nombre_usuario']