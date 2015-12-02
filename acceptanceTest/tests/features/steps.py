# -*- coding: utf-8 -*-
from lettuce import *
from lxml import html
from nose.tools import assert_equals

@before.all
def set_browser():
    world.browser = webdriver.Firefox()
#Código para agregar un cliente nuevo
@step(r'Dado que el cliente "([^"]*)" no se encuentra registrado')
def Dado_que_el_cliente_group1_no_se_encuentra_registrado(step, cliente):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'Cuando hago clic en el boton crear')
def Cuando_hago_clic_en_el_boton_crear(step):
    pass

@step(r'Entonces debo ser capaz de ver el mensaje"([^"]*)"')
def Entonces_debo_ser_capaz_de_ver_el_mensaje_group1(step, texto):
    assert "" == texto
#Código para consultar los datos de un cliente
@step(r'Dado que el cliente "([^"]*)" se encuentra registrado en el sistema')
def Dado_que_el_cliente_group1_se_encuentra_registrado_en_el_sistema(step, cliente):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'Cuando hago clic en el boton consultar')
def Cuando_hago_clic_en_el_boton_consultar(step):
    pass

@step(r'Entonces debo ser capaz de ver el mensaje"([^"]*)"')
def Entonces_debo_ser_capaz_de_ver_el_mensaje_group1(step, texto):
    assert "" == texto

#Código para eliminar los datos de un cliente
@step(r'Dado que el cliente "([^"]*)" se encuentra registrado en el sistema')
def Dado_que_el_cliente_group1_se_encuentra_registrado_en_el_sistema(step, cliente):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'Cuando hago clic en el boton eliminar')
def Cuando_hago_clic_en_el_boton_eliminar(step):
    pass

@step(r'Entonces debo ser capaz de ver el mensaje"([^"]*)"')
def Entonces_debo_ser_capaz_de_ver_el_mensaje_group1(step, texto):
    assert "" == texto

#Código para modificar los datos de un cliente
@step(r'Dado que el cliente "([^"]*)" se encuentra registrado en el sistema')
def Dado_que_el_cliente_group1_se_encuentra_registrado_en_el_sistema(step, cliente):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'Cuando hago clic en el boton modificar')
def Cuando_hago_clic_en_el_boton_modificar(step):
    pass

@step(r'Entonces debo ser capaz de ver el mensaje"([^"]*)"')
def Entonces_debo_ser_capaz_de_ver_el_mensaje_group1(step, texto):
    assert "" == texto
