# -*- coding: utf-8 -*-
from lettuce import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
id_proveedor = 0


@before.all
def set_browser():
    #browser = webdriver.Firefox()
    browser.get('http://localhost:8000')


@step(u'Given Que la compra "([^"]*)" esta en proceso')
def given_que_la_compra_group1_esta_en_proceso(step, group1):
    # Probaré google
    browser.get('http://localhost:8000/compras/nueva_compra.html')


@step(u'When Oprimo el botón de cancelar compra')
def when_oprimo_el_boton_de_cancelar_compra(step):
    boton = browser.find_element_by_id("btn_cancelar")
    boton.clic()


@step(u'Then Puedo ver una lista con las compras que he realizado')
def then_puedo_ver_una_lista_con_las_compras_que_he_realizado(step):
    listaCompras = browser.find_elements('compra')
    assert listaCompras.length > 0
    # assertTrue


@step(u'Given Que he ingresado al sistema como "([^"]*)" y me encuentro en la pagina principal')
def given_que_he_ingresado_al_sistema_como_group1_y_me_encuentro_en_la_pagina_principal(step, group1):
    browser.get('http://localhost:8080/principal/')


@step(u'When Oprimo el botón de ver proveedores')
def when_oprimo_el_boton_de_ver_proveedores(step):
    boton_ver_proveedores = browser.find_element_by_id('btn_ver_proveedores')
    boton_ver_proveedores.clic()


@step(u'Then Puedo ver los proveedores registrados en una lista "([^"]*)"')
def then_puedo_ver_los_proveedores_registrados_en_una_lista_group1(step, group1):
    lista_proveedores = browser.find_elements('proveedor')
    assert lista_proveedores.length > 0


@step(u'Given El proveedor "([^"]*)" se encuentra registrado en el sistema')
def given_el_proveedor_group1_se_encuentra_registrado_en_el_sistema(step, group1):
    browser.get('http://localhost:8000/proveedores/')
    proveedores = browser.find_elements('proveedor')
    for p in proveedores:
        if p.text == group1:
            id_proveedor = p.id


@step(u'When Oprimo el botón de elminar proveedor')
def when_oprimo_el_boton_de_elminar_proveedor(step):
    btn_eliminar = browser.find_element_by_id('btn_eliminar_' + id_proveedor)
    btn_eliminar.clic()


@step(u'Then Puedo ver una lista con los proveedores registrados')
def then_puedo_ver_una_lista_con_los_proveedores_registrados(step):
    lista_proveedores = browser.find_elements('proveedor')
    assert lista_proveedores.length > 0


@step(u'Given Que hoy es "([^"]*)"')
def given_que_hoy_es_group1(step, group1):
    browser.get('http://localhost:8000/principal/')


@step(u'When Oprimo el botón de menu del día')
def when_oprimo_el_boton_de_menu_del_dia(step):
    boton_menu_del_dia = browser.find_element_by_id('btn_menu_dia')
    boton_menu_del_dia.clic()


@step(u'Then Puedo ver "([^"]*)" en la pantalla')
def then_puedo_ver_group1_en_la_pantalla(step, group1):
    texto_menu_dia = browser.find_element_by_id('title_menu_dia')
    assert texto_menu_dia.text == group1


@step(u'Given Que el proveedor "([^"]*)" se encuentra registrado AND me encuentro en la pantalla de editar')
def given_que_el_proveedor_group1_se_encuentra_registrado_and_me_encuentro_en_la_pantalla_de_editar(step, group1):
    browser.get('http://localhost:8000/proveedores/1/editar/')


@step(u'When Cambio el nombre por "([^"]*)" AND hago clic en el boton de modificar')
def when_cambio_el_nombre_por_group1_and_hago_clic_en_el_boton_de_modificar(step, group1):
    caja_texto_nombre = browser.find_element_by_id('cj_nombre')
    caja_texto_nombre.send_keys(group1)
    boton_modificar = browser.find_element_by_id('btn_guardar')
    boton_modificar.clic()


@step(u'Then Puedo ver en la lista de proveedores registrados al proveedor "([^"]*)"')
def then_puedo_ver_en_la_lista_de_proveedores_registrados_al_proveedor_group1(step, group1):
    lista_proveedores = browser.find_elements_by_id('proveedor')
    assert lista_proveedores.length > 0


@step(u'Given Que me encuentro en la pagina principal como empleado')
def given_que_me_encuentro_en_la_pagina_principal_como_empleado(step):
    browser.get('http://localhost:8000/principal.html')


@step(u'When Oprimo el botón de nuevo proveedor')
def when_oprimo_el_boton_de_nuevo_proveedor(step):
    boton_nuevo_proveedor = browser.find_element_by_id('btn_nuevo_proveedor')
    boton_nuevo_proveedor.clic()


@step(u'Then Puedo ver el mensaje "([^"]*)"')
def then_puedo_ver_el_mensaje_group1(step, group1):
    texto_nuevo_proveedor = browser.find_element_by_id('txt_nuevo_proveedor')
    assert texto_nuevo_proveedor == group1


@step(u'Given Que hoy es día de promociones')
def given_que_hoy_es_dia_de_promociones(step):
    browser.get('http://localhost:8000/compras/nueva_compra/')


@step(u'When Oprimo el botón de ver promociones')
def when_oprimo_el_boton_de_ver_promociones(step):
    boton_ver_promociones = browser.find_element_by_id('btn_ver_promociones')
    boton_ver_promociones.clic()


@step(u'Then Puedo ver una lista con los productos que tienen promocion')
def then_puedo_ver_una_lista_con_los_productos_que_tienen_promocion(step):
    lista_productos = browser.find_elements_by_id('productos')
    assert lista_productos.length > 0


@step(u'Given Que he ingresado como cliente de la cafeteria')
def given_que_he_ingresado_como_cliente_de_la_cafeteria(step):
    browser.get('http://localhost:8000/principal/')


@step(u'When Oprimo el botón de nueva compra')
def when_oprimo_el_boton_de_nueva_compra(step):
    boton_nueva_compra = browser.find_element_by_id('btn_nueva_compra')
    boton_nueva_compra.clic()


@step(u'Then Puedo ver mi numero de compra que estoy por realizar')
def then_puedo_ver_mi_numero_de_compra_que_estoy_por_realizar(step):
    numero_compra = browser.find_element_by_id('id_compra')
    assert numero_compra.text != ""


@step(u'Given Que he ingresado al sistema como "([^"]*)"')
def given_que_he_ingresado_al_sistema_como_group1(step, group1):
    browser.get('http://localhost:8000/principal/')


@step(u'When Oprimo el botón de historial de compras')
def when_oprimo_el_boton_de_historial_de_compras(step):
    boton_historial_compras = browser.find_element_by_id(
        'btn_historial_compras')
    boton_historial_compras.clic()


@step(u'Then Puedo ver "([^"]*)" por "([^"]*)"')
def then_puedo_ver_group1_por_group2(step, group1, group2):
    texto_principal = browser.find_element_by_id('txt_titulo')
    assert texto_principal.text == group1


@after.all
def tearDown(self):
    browser.quit()
