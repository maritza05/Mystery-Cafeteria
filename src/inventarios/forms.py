# coding: utf-8 
from django import forms
from Inventario.models import Inventario

class InventarioForm(forms.ModelForm):
    """Formulario para dar servicio a Inventario"""
    class Meta(object):
        model = Inventario
        fields = ['id_producto', 'cantidad']
