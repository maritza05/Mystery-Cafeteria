# -*- coding: utf-8 -*-
from lettuce import step
from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()


@before.all
def set_browser():
    browser.get('http://localhost:8000')
#Código para agregar un empleado nuevo
@step(u'Dado que me encuentro en la pagina principal como administrador')
def Dado_que_me_encuentro_en_la_pagina_principal_como_administrador(step):
    browser.get('http://localhost:8000/principal.html')

@step(u'Cuando hago clic en el boton nuevo empleado')
def Cuando_hago__clic_en_el_boton_nuevo_empleado(step):
    boton_nuevo_empleado = browser.find_element_by_id('btn_nuevo_empleado')
    boton_nuevo_empleado.clic()
@step(u'Entonces debo ser capaz de ver un mensaje "([^"]*)"')
def Entonces_debo_ser_capaz_de_ver_un_mensaje_group1(step, group1):
    mns_nuevo_empleado = browser.find_element_by_id('mns_nuevo_empleado')
    assert mns_nuevo_empleado == group1

#Código para consultar los datos de un empleado
@step(u'Dado que he ingresado al sistema como administrador')
def Dado_que_he_ingresado_al_sistema_como_administrador(step):
   browser.get('http://localhost:8000/empleado/')
   empleado = browser.find_elements('empleado')
   for e in empleado:
        if e.text == group1:
            id_empleado = e.id

@step(u'Cuando hago clic en el boton consultar')
def Cuando_hago_clic_en_el_boton_consultar(step):
    boton_consultar_empleado = browser.find_element_by_id('btn_consultar_' + id_empleado)
    boton_consultar_empleado.clic()

@step(u'Entonces debo ser capaz de ver el mensaje "([^"]*)"')
def Entonces_debo_ser_capaz_de_ver_el_mensaje_group1(step, texto):
    lista_empleado = browser.find_elements('empleados')
    assert lista_empleado.length > 0

#Código para eliminar los datos de un empleado
@step(u'Dado que el empleado "([^"]*)" se encuentra registrado en el sistema')
def Dado_que_el_empleado_group1_se_encuentra_registrado_en_el_sistema(step, empleado):
   browser.get('http://localhost:8000/clientes/')
   empleados = browser.find_elements('empleados')
   for e in empleado:
        if e.text == group1:
            id_empleado = e.id

@step(u'Cuando hago clic en el boton eliminar empleado')
def Cuando_hago_clic_en_el_boton_eliminar_empleado(step):
    boton_eliminar_empleado = browser.find_element_by_id('btn_eliminar_' + id_empleado)
    boton_eliminar_empleado.clic()

@step(u'Entonces debo ser capaz de ver la lista con los empleados')
def Entonces_debo_ser_capaz_de_ver_la_lista_con_los_empleados(step):
    lista_empleados = browser.find_elements('empleados')
    assert lista_empleados.length > 0

#Código para modificar los datos de un empleado
@step(u'Dado que el empleado "([^"]*)" se encuentra registrado AND me encuentro en la pantalla de editar')
def dado_que_el_empleado_group1_se_encuentra_registrado_and_me_encuentro_en_la_pantalla_de_editar(step, group1):
    browser.get('http://localhost:8000/clientes/1/editar/')


@step(u'Cuando cambio el nombre por "([^"]*)" AND hago clic en el boton de modificar')
def cuando_cambio_el_nombre_por_group1_and_hago_clic_en_el_boton_de_modificar(step, group1):
    txt_nombre_empleado = browser.find_element_by_id('txt_nombre')
    txt_nombre_empleado.send_keys(group1)
    boton_modificar_empleado= browser.find_element_by_id('btn_guardar_cambios')
    boton_modificar_empleado.clic()


@step(u'Entonces puedo ver en la lista actualizada de empleados con el empleado "([^"]*)"')
def entonces_puedo_ver_la_lista_de_actualiza_de_empleados_con_el_empleado_group1(step, group1):
    lista_empleados = browser.find_elements_by_id('empleados')
    assert lista_empleados.length > 0



@after.all
def tearDown(self):
    browser.quit()
