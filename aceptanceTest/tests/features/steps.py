# -*- coding: utf-8 -*-
from lettuce import *


@before.all
def set_browser():
    pass


@step(r'Given la compra "([^"]*)" esta en proceso')
def Given_la_compra_group1_esta_en_proceso(step, compra):
    pass


@step(r'When Oprimo el boton de cancelar')
def When_Oprimo_el_boton_de_cancelar(step):
    # Solicitar cancelar compra
    pass


@step(r'Then Puedo ver el mensaje "([^"]*)"')
def Then_Puedo_ver_el_mensaje_group1(step, texto):
    pass


@step(r'Given Que hoy es "([^"]*)"')
def Given_Que_hoy_es_group1(step, dia):
    pass


@step(r'When Oprimo el botón de menu')
def When_Oprimo_el_boton_de_menu(step):
    pass


@step(r'When Oprimo el botón de promociones')
def When_Oprimo_el_boton_de_promociones(step):
    pass


@step(r'Given Que estoy realizando la compra "([^"]*)"')
def Given_Que_estoy_realizando_la_compra_group1(step, id_compra):
    pass


@step(r'When Oprimo el boton de comprar')
def When_Oprimo_el_boton_de_comprar(step, id_compra):
    pass


@step(r'Then Puedo ver la opcion de "([^"]*)"')
def Then_Puedo_ver_la_opcion_de_group1(step, texto):
    pass


@step(r'Given Que he ingresado al sistema con el usuario "([^"]*)" y la contraseña "([^"]*)"')
def Given_Que_he_ingresado_al_sistema_como_group1(step, usuario, password):
    pass


@step(r'When Oprimo el botón de historial de compras')
def Then_Puedo_ver_la_opcion_de_group1(step):
    pass


@step(r'Given Que he ingresado al sistema como "([^"]*)"')
def Given_Que_he_ingresado_al_sistema_como_group1(step, usuario):
    pass


@step(r'When Oprimo el botón de proveedores')
def When_Oprimo_el_boton_de_proveedores(step):
    pass


@step(r'Then Puedo ver el mensaje "([^"]*)"')
def Then_Puedo_ver_el_mensaje_group1(step, texto):
    pass


@step(r'When Oprimo el botón de ver proveedor')
def When_Oprimo_el_boton_de_ver_proveedor(step):
    pass


@step(r'Given El proveedor "([^"]*)" se encuentra registrado')
def Given_El_proveedor_group1_se_encuentra_registrado(step, proveedor):
    pass


@step(r'When Oprimo el botón de eliminar')
def When_Oprimo_el_boton_de_eliminar(step):
    pass


@step(r'Then Ya no puedo ver el proveedor "([^"]*)" en la lista de proveedores')
def Then_Ya_no_puedo_ver_el_proveedor_group1_en_la_lista_de_proveedores(step, proveedor):
    pass


@step(r'When Cambio el nombre por "([^"]*)" AND hago clic en el boton de modificar')
def When_Cambio_el_nombre_por_group1_AND_hago_clic_en_el_boton_de_modificar(step, modificar):
    pass


@step(r'When Oprimo el botón de nuevo proveedor')
def When_Oprimo_el_boton_de_nuevo_proveedor(step):
    pass


@step(r'Given Que he ingresado como "([^"]*)" y me encuentro en nuevo proveedor')
def Given_Que_he_ingresado_como_group1_y_me_encuentro_en_nuevo_proveedor(step, usuario):
    pass


@step(r'When Introduzco los datos "([^"]*)", "([^"]*)" AND Hago clic en el boton guardar')
def When_Introduzco_los_datos_group1_group2_AND_Hago_clic_en_el_boton_guardar(step, nombre, direccion):
    pass


@step(u'When Oprimo el botón de cancelar')
def when_oprimo_el_boton_de_cancelar(step):
    assert False, 'This step must be implemented'


@step(u'When Oprimo el botón de proveedores')
def when_oprimo_el_boton_de_proveedores(step):
    assert False, 'This step must be implemented'


@step(u'When Oprimo el botón de ver proveedor')
def when_oprimo_el_boton_de_ver_proveedor(step):
    assert False, 'This step must be implemented'


@step(u'When Oprimo el botón de elminar')
def when_oprimo_el_boton_de_elminar(step):
    assert False, 'This step must be implemented'


@step(u'When Oprimo el botón de menu')
def when_oprimo_el_boton_de_menu(step):
    assert False, 'This step must be implemented'


@step(u'Given Que el proveedor "([^"]*)" se encuentra registrado')
def given_que_el_proveedor_group1_se_encuentra_registrado(step, group1):
    assert False, 'This step must be implemented'


@step(u'Given Que he ingresado como "([^"]*)"')
def given_que_he_ingresado_como_group1(step, group1):
    assert False, 'This step must be implemented'


@step(u'When Oprimo el botón de nuevo proveedor')
def when_oprimo_el_boton_de_nuevo_proveedor(step):
    assert False, 'This step must be implemented'


@step(u'When Introduzco los datos "([^"]*)", "([^"]*)" AND Hago clic el botón guardar')
def when_introduzco_los_datos_group1_group2_and_hago_clic_el_boton_guardar(step, group1, group2):
    assert False, 'This step must be implemented'


@step(u'When Introduzco los datos ""([^"]*)"" AND Hago clic el botón guardar')
def when_introduzco_los_datos_group1_and_hago_clic_el_boton_guardar(step, group1):
    assert False, 'This step must be implemented'


@step(u'When Oprimo el botón de promociones')
def when_oprimo_el_boton_de_promociones(step):
    assert False, 'This step must be implemented'


@step(u'When Oprimo el botón de comprar')
def when_oprimo_el_boton_de_comprar(step):
    assert False, 'This step must be implemented'


@step(u'When Oprimo el botón de historial de compras')
def when_oprimo_el_boton_de_historial_de_compras(step):
    assert False, 'This step must be implemented'
