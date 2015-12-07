# -*- encoding: utf-8 -*-
from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

@before.all
def set_browser():
    world.driver = webdriver.Firefox()

@step(r'Que accedo a la url "([^"]*)"')
def access_url(step, url):
    world.driver.get(url)

@step(r'veo el encabezado "([^"]*)"')
def see_header(step, text):
    header = world.driver.title
    assert header == text

# Pruebas para el registro de un nuevo usuario
@step(u'Given Que accedo a la url del formulario "([^"]*)"')
def given_que_accedo_a_la_url_del_formulario(step, url):
    world.driver.get(url)

@step(u'Then veo una caja de texto para ingresar el usuario e ingreso "([^"]*)"')
def then_veo_una_caja_de_texto_para_ingresar_el_usuario_e_ingreso(step, username):
    caja_usuario = world.driver.find_element_by_id("id_username")
    caja_usuario.send_keys(username)

@step(u'And veo una caja de texto para el correo e ingreso "([^"]*)"')
def and_veo_una_caja_de_texto_para_el_correo_e_ingreso(step, email):
    caja_email = world.driver.find_element_by_id("id_email")
    caja_email.send_keys(email)

@step(u'And veo una caja de texto para el password e ingreso "([^"]*)"')
def and_veo_una_caja_de_texto_para_el_password_e_ingreso(step, password):
    caja_password = world.driver.find_element_by_id("id_password1")
    caja_password.send_keys(password)

@step(u'And veo una caja de texto para la confirmacion del password e ingreso "([^"]*)"')
def and_veo_una_caja_de_texto_para_la_confirmacion_del_password_e_ingreso(step, password):
    caja_password_confirmacion = world.driver.find_element_by_id("id_password2")
    caja_password_confirmacion.send_keys(password)

@step(u'And doy clic en el botón de registrar')
def and_doy_clic_en_el_boton_de_registrar(step):
    world.driver.find_element(By.XPATH, "//input[@value='Register']").click()
    
@step(u'And veo un mensaje "([^"]*)"')
def and_veo_un_mensaje_group1(step, mensaje_registro):
	time.sleep(10)
	heading_registration = world.driver.find_element_by_tag_name('h1')
	assert heading_registration.text == mensaje_registro