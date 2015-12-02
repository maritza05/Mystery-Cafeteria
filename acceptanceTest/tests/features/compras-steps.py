# -*- coding: utf-8 -*-
from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals

@before.all
def set_browser():
    world.browser = Client()

@step(r'Dado que realice la compra "001"')
def obtener_compra_realizada(step, compra):
    #Codigo para realizar compra
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'Cuando solicito "cancelar compra" y acepto cancelar la compra')
def cancelar_compra(step):
    #Solicitar cancelar compra
    pass

@step(r'Entonces el resultado debe ser "Compra cancelada"')
def comprobar_cancelacion_de_compra(step, texto):
    assert "" == texto
