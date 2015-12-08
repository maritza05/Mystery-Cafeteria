#coding: utf-8
from django import forms
from puestos.models import Puesto


class PuestoForm(forms.ModelForm):

    class Meta(object):
        model = Puesto
        fields = ['puesto']
