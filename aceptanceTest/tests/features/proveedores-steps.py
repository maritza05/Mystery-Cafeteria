# -*- coding: utf-8 -*-
from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals

@before.all
def set_browser():
    world.browser = Client()

@step(r'Given Que he ingresado al sistema como "([^"]*)"')
def Given_Que_he_ingresado_al_sistema_como_group1(step, usuario):
    #Codigo para realizar compra
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'When Oprimo el botón de proveedores')
def When_Oprimo_el_boton_de_proveedores(step):
    #Codigo para realizar compra
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'Then Puedo ver el mensaje "([^"]*)"')
def Then_Puedo_ver_el_mensaje_group1(step, texto):
    #Codigo para realizar compra
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)
    assert "" == texto

@step(r'When Oprimo el botón de ver proveedor')
def When_Oprimo_el_boton_de_ver_proveedor(step):
    #Codigo para realizar compra
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'Given El proveedor "([^"]*)" se encuentra registrado')
def Given_El_proveedor_group1_se_encuentra_registrado(step, proveedor):
    #Codigo para realizar compra
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)
    assert "" == proveedor

@step(r'When Oprimo el botón de eliminar')
def When_Oprimo_el_boton_de_eliminar(step):
    #Codigo para realizar compra
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'Then Ya no puedo ver el proveedor "([^"]*)" en la lista de proveedores')
def Then_Ya_no_puedo_ver_el_proveedor_group1_en_la_lista_de_proveedores(step, proveedor):
    #Codigo para realizar compra
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)
    assert "" == proveedor

@step(r'When Cambio el nombre por "([^"]*)" AND hago clic en el boton de modificar')
def When_Cambio_el_nombre_por_group1_AND_hago_clic_en_el_boton_de_modificar(step, modificar):
    #Codigo para realizar compra
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)
    assert "" == proveedor

@step(r'When Oprimo el botón de nuevo proveedor')
def When_Oprimo_el_boton_de_nuevo_proveedor(step):
    #Codigo para realizar compra
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

step(r'Given Que he ingresado como "([^"]*)" y me encuentro en nuevo proveedor')
def Given_Que_he_ingresado_como_group1_y_me_encuentro_en_nuevo_proveedor(step, usuario):
    #Codigo para realizar compra
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)
    assert "" == proveedor

@step(r'When Introduzco los datos "([^"]*)", "([^"]*)" AND Hago clic en el boton guardar')
def When_Introduzco_los_datos_group1_group2_AND_Hago_clic_en_el_boton_guardar(step, nombre, direccion):
    #Codigo para realizar compra
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)
    assert "" == proveedor