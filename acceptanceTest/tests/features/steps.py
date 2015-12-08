# -*- coding: utf-8 -*-
from lettuce import step
from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()


@before.all
def set_browser():
    browser.get('http://localhost:8000')
#Código para agregar un puesto nuevo
@step(u'Dado que me encuentro en la pagina principal como administrador')
def Dado_que_me_encuentro_en_la_pagina_principal_como_administrador(step):
    browser.get('http://localhost:8000/principal.html')

@step(u'Cuando hago clic en el boton nuevo puesto')
def Cuando_hago__clic_en_el_boton_nuevo_puesto(step):
    boton_nuevo_puesto = browser.find_element_by_id('btn_nuevo_puesto')
    boton_nuevo_puesto.clic()
@step(u'Entonces debo ser capaz de ver un mensaje "([^"]*)"')
def Entonces_debo_ser_capaz_de_ver_un_mensaje_group1(step, group1):
    mns_nuevo_puesto = browser.find_element_by_id('mns_nuevo_puesto')
    assert mns_nuevo_puesto == group1

#Código para consultar los datos de un puesto
@step(u'Dado que he insgresado al sistema como administrador')
def Dado_que_he_insgresado_al_sistema_como_administrador(step):
   browser.get('http://localhost:8000/puesto/')
   puesto = browser.find_elements('puesto')
   for p in puesto:
        if p.text == group1:
            id_puesto = p.id

@step(u'Cuando hago clic en el boton consultar')
def Cuando_hago_clic_en_el_boton_consultar(step):
    boton_consultar_puesto = browser.find_element_by_id('btn_consultar_' + id_puesto)
    boton_consultar_puesto.clic()

@step(u'Entonces debo ser capaz de ver el mensaje "([^"]*)"')
def Entonces_debo_ser_capaz_de_ver_el_mensaje_group1(step, texto):
    ista_puesto = browser.find_elements('puestos')
    assert lista_puesto.length > 0

#Código para eliminar los datos de un puesto
@step(u'Dado que el puesto "([^"]*)" se encuentra registrado en el sistema')
def Dado_que_el_puesto_group1_se_encuentra_registrado_en_el_sistema(step, puesto):
   browser.get('http://localhost:8000/clientes/')
   puestos = browser.find_elements('puestos')
   for p in puestos:
        if p.text == group1:
            id_puestos = p.id

@step(u'Cuando hago clic en el boton eliminar puesto')
def Cuando_hago_clic_en_el_boton_eliminar_puesto(step):
    boton_eliminar_puesto = browser.find_element_by_id('btn_eliminar_' + id_puesto)
    boton_eliminar_puesto.clic()

@step(u'Entonces debo ser capaz de ver la lista con los puestos')
def Entonces_debo_ser_capaz_de_ver_la_lista_con_los_puestos(step):
    lista_puesto = browser.find_elements('puestos')
    assert lista_puesto.length > 0

#Código para modificar los datos de un puesto
@step(u'Dado que el puesto "([^"]*)" se encuentra registrado AND me encuentro en la pantalla de editar')
def dado_que_el_puesto_group1_se_encuentra_registrado_and_me_encuentro_en_la_pantalla_de_editar(step, group1):
    browser.get('http://localhost:8000/clientes/1/editar/')


@step(u'Cuando cambio el nombre por "([^"]*)" AND hago clic en el boton de modificar')
def cuando_cambio_el_nombre_por_group1_and_hago_clic_en_el_boton_de_modificar(step, group1):
    txt_nombre_puesto = browser.find_element_by_id('txt_nombre')
    txt_nombre_puesto.send_keys(group1)
    boton_modificar_puesto = browser.find_element_by_id('btn_guardar_cambios')
    boton_modificar_puesto.clic()


@step(u'Entonces puedo ver en la lista actualizada de puestos con el puesto "([^"]*)"')
def entonces_puedo_ver_la_lista_de_actualiza_de_puestos_con_el_puesto_group1(step, group1):
    lista_puesto = browser.find_elements_by_id('puestos')
    assert lista_puesto.length > 0



@after.all
def tearDown(self):
    browser.quit()
