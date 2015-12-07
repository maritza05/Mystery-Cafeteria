# coding: utf-8 #
from django import forms
from proveedores.models import Proveedor


class ProveedorForm(forms.ModelForm):

    class Meta(object):
        model = Proveedor
        fields = ['organizacion', 'email', 'numero_telefono']
