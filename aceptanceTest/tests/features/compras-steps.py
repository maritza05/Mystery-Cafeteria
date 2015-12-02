# -*- coding: utf-8 -*-
from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals

@before.all
def set_browser():
    world.browser = Client()

@step(r'Given la compra "([^"]*)" esta en proceso')
def Given_la_compra_group1_esta_en_proceso(step, compra):
    #Codigo para realizar compra
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'When Oprimo el boton de cancelar')
def When_Oprimo_el_boton_de_cancelar(step):
    #Solicitar cancelar compra
    pass

@step(r'Then Puedo ver el mensaje "([^"]*)"')
def Then_Puedo_ver_el_mensaje_group1(step, texto):
    assert "" == texto

@step(r'Given Que hoy es "([^"]*)"')
def Given_Que_hoy_es_group1(step, dia):
    assert "" == texto

@step(r'When Oprimo el botón de menu')
def When_Oprimo_el_boton_de_menu(step):
    assert "" == texto

@step(r'When Oprimo el botón de promociones')
def When_Oprimo_el_boton_de_promociones(step):
    assert "" == texto

@step(r'Given Que estoy realizando la compra "([^"]*)"')
def Given_Que_estoy_realizando_la_compra_group1(step, id_compra):
    assert "" == texto

@step(r'When Oprimo el boton de comprar')
def When_Oprimo_el_boton_de_comprar(step, id_compra):
    assert "" == texto

@step(r'Then Puedo ver la opcion de "([^"]*)"')
def Then_Puedo_ver_la_opcion_de_group1(step, texto):
    assert "" == texto

@step(r'Given Que he ingresado al sistema con el usuario "([^"]*)" y la contraseña "([^"]*)"')
def Given_Que_he_ingresado_al_sistema_como_group1(step, usuario, password):
    assert "" == texto

@step(r'When Oprimo el botón de historial de compras')
def Then_Puedo_ver_la_opcion_de_group1(step):
    assert "" == texto
