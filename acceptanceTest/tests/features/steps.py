# -*- coding: utf-8 -*-
from lettuce import step
from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()


@before.all
def set_browser():
    browser.get('http://localhost:8000')
#Código para agregar un cliente nuevo
@step(u'Given que me encuentro en la pagina principal como cliente')
def given_que_me_encuentro_en_la_pagina_principal_como_cliente(step):
    browser.get('http://localhost:8000/principal.html')

@step(u'When hago clic en el boton nuevo cliente')
def when_hago__clic_en_el_boton_nuevo_cliente(step):
    boton_nuevo_cliente = browser.find_element_by_id('btn_nuevo_cliente')
    boton_nuevo_cliente.clic()
@step(u'Then debo ser capaz de ver un mensaje "([^"]*)"')
def then_debo_ser_capaz_de_ver_un_mensaje_group1(step, group1):
    mns_nuevo_cliente = browser.find_element_by_id('mns_nuevo_cliente')
    assert mns_nuevo_cliente == group1

#Código para agregar un cliente ya existente
@step(u'Dado que me encuentro en la pagina principal como cliente')
def Dado_que_me_encuentro_en_la_pagina_principal_como_cliente(step):
    browser.get('http://localhost:8000/principal.html')

@step(u'Cuando hago clic en el boton nuevo cliente')
def Cuando_hago_clic_en_el_boton_nuevo_cliente(step):
    boton_nuevo_cliente = browser.find_element_by_id('btn_nuevo_cliente')
    boton_nuevo_cliente.clic()
@step(u'Entonces debo ser capaz de ver el mensaje"([^"]*)"')
def Entonces_debo_ser_capaz_de_ver_el_mensaje_group1(step, group1):
    mns_nuevo_cliente = browser.find_element_by_id('mns_nuevo_cliente')
    assert mns_nuevo_cliente == group1

#Código para consultar los datos de un cliente
@step(u'Dado que he insgresado al sistema como empleado')
def Dado_que_he_ingresado_al_sistema_como_empleado(step):
   browser.get('http://localhost:8000/clientes/')
   clientes = browser.find_elements('clientes')
   for c in clientes:
        if c.text == group1:
            id_clientes = c.id

@step(u'Cuando hago clic en el boton consultar')
def Cuando_hago_clic_en_el_boton_consultar(step):
    boton_consultar_cliente = browser.find_element_by_id('btn_consultar_' + id_clientes)
    boton_consultar_clientes.clic()

@step(u'Entonces debo ser capaz de ver el mensaje"([^"]*)"')
def Entonces_debo_ser_capaz_de_ver_el_mensaje_group1(step, texto):
    ista_clientes = browser.find_elements('clientes')
    assert lista_clientes.length > 0

#Código para eliminar los datos de un cliente
@step(u'Dado que el cliente "([^"]*)" se encuentra registrado en el sistema')
def Dado_que_el_cliente_group1_se_encuentra_registrado_en_el_sistema(step, cliente):
   browser.get('http://localhost:8000/clientes/')
   clientes = browser.find_elements('clientes')
   for c in clientes:
        if c.text == group1:
            id_clientes = c.id

@step(u'Cuando hago clic en el boton eliminar cliente')
def Cuando_hago_clic_en_el_boton_eliminar_cliente(step):
    boton_eliminar_cliente = browser.find_element_by_id('btn_eliminar_' + id_clientes)
    boton_eliminar_clientes.clic()

@step(u'Entonces debo ser capaz de ver la lista con los clientes')
def Entonces_debo_ser_capaz_de_ver_la_lista_con_los_clientes(step):
    lista_clientes = browser.find_elements('clientes')
    assert lista_clientes.length > 0

#Código para modificar los datos de un cliente
@step(u'Given que el cliente "([^"]*)" se encuentra registrado AND me encuentro en la pantalla de editar')
def given_que_el_cliente_group1_se_encuentra_registrado_and_se_encuentra_en_la_pantalla_de_editar(step, group1):
    browser.get('http://localhost:8000/clientes/1/editar/')


@step(u'When cambio el nombre por "([^"]*)" AND hago clic en el boton de modificar')
def when_cambio_el_nombre_por_group1_and_hago_clic_en_el_boton_de_modificar(step, group1):
    txt_nombre_cliente = browser.find_element_by_id('txt_nombre')
    txt_nombre_cliente.send_keys(group1)
    boton_modificar_cliente = browser.find_element_by_id('btn_guardar_cambios')
    boton_modificar_cliente.clic()


@step(u'Then puedo ver en la lista actualizada de clientes con el cliente "([^"]*)"')
def then_puedo_ver_la_lista_de_actualiza_de_clientes_con_el_cliente_group1(step, group1):
    lista_clientes = browser.find_elements_by_id('clientes')
    assert lista_clientes.length > 0



@after.all
def tearDown(self):
    browser.quit()
