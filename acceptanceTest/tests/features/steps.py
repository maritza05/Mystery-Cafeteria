from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@before.all
def set_browser():
    world.browser = webdriver.Firefox()

@step(r'acceso a la URL Productos"([^"]*)"')
def access_url(step, url):
    world.browser.get('http://localhost:8000/Productos')
    url = broser.title('Catalogo Productos')
    assert url

@step(r'Cuando hago clic en el boton añadir producto')
def Cuando_hago_click_anadir_producto(step):
    boton_nuevo_producto = browser.find_element_by_id('btn_nuevo_producto'+ id_producto)
    boton_nuevo_producto.click()

@step(r'Cuando hago clic en el boton modificar producto')
def Cuando_hago_click_en_modificar_producto(step):
    boton_modificar_producto = browser.find_element_by_id('btn_modificar_producto' +id_producto)
    boton_modificar_producto.click()

@step(r'Dado que quiero añadir nombre producto existente')
def Dado_que_quiero_anadir_producto_existente_regresa_productos(step)
    browser.get('http://localhost:8000/Productos/')

@step(r'Dado que envie formulario con campos vacios')
def Dado_que_envie_formulario_vacio_regresa_a_productos(step)
    browser.get('http://localhost:8000/Productos/')

@step(r'Dado que envie formulario correctamente)
def Dado_que_envie_formulario_correctamente(step)
    browser.get('http://localhost:8000/Productos/3/anadir')
    

@after.all
def tearDown(self):
    browser.quit()

