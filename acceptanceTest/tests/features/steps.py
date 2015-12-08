from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@before.all
def set_browser():
    world.browser = webdriver.Firefox()

@step(r'Quiero consultar Inventario"([^"]*)"')
def access_url(step, url):
    world.browser.get('http://localhost:8000/Invetario')
    url = broser.find_element_by_id('title')
    assert title = Invetario

@step(r'Cuando hago clic en el boton añadir invetario')
def Cuando_hago_clic_en_anadir_inventario(step):
    boton_anadir_invetario = browser.find_element_by_id('btn_anadir_producto' )
    boton_anadir_invetario.click()
    broser.get('http://localhost:8000/Inventario/Anadir')

@step(r'Cuando hago clic en el boton editar invetario')
def Cuando_hago_click_en_restar_inventario(step):
    boton_restar_invetario = browser.find_element_by_id('btn_restar_inventario')
    boton_restar_invetario.click()
    broser.get('https://localhost:8000/Inventario/Restar')

@step(r'Cuando hago clic en el boton añadir invetario')
def Cuando_hago_clic_en_anadir_inventario_regresa_inventario(step):
    boton_anadir_invetario = browser.find_element_by_id('btn_anadir_producto' + id_producto)
    boton_anadir_invetario.click()
    broser.get('http://localhost:8000/Inventario/')

@step(r'Cuando hago clic en el boton editar invetario')
def Cuando_hago_click_en_restar_inventario_regresa_inventario(step):
    boton_restar_invetario = browser.find_element_by_id('btn_restar_inventario' + id_producto)
    boton_restar_invetario.click()
    broser.get('https://localhost:8000/Inventario')

@after.all
def tearDown(self):
    browser.quit()
