# coding: utf-8 #
from django import forms
from compras.models import Compra


class CompraForm(forms.ModelForm):

    class Meta(object):
        model = Compra
        fields = ['id_proveedor', 'id_empleado', 'id_inventario', 'fecha', 'monto']
