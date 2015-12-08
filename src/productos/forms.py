# coding: utf-8 
from django import forms
from productos.models import Producto

class ProductoForm(forms.ModelForm):
    """Formulario para dar servicio al pagina producto"""
    class Meta(object):
        model = Producto
        fields = ['nombre', 'descripcion','precio']
