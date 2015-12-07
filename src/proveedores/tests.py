from django.test import TestCase
from django.core.urlresolvers import resolve
from proveedores.views import listar, nuevo_proveedor, eliminar_proveedor, editar_proveedor
from django.http import HttpRequest


class ProveedoresTest(TestCase):

    def probar_la_url_de_listar_proveedores(self):
        found = resolve('/')
        self.assertEqual(found.func, listar)

    def probar_la_url_de_agregar_nuevo_proveedor(self):
        found = resolve('/nuevo_proveedor')
        self.assertEqual(found.func, nuevo_proveedor)

    def probar_la_url_de_eliminar_proveedor(self, id_proveedor_eliminar):
        found = resolve('/' + id_proveedor_eliminar + '/eliminar')
        self.assertEqual(found.func, eliminar_proveedor)

    def probar_si_listar_devuelve_los_datos_esperados(self):
        request = HttpRequest()
        response = listar(request)
        self.assertTrue(response.content.endswith('</html>'))

    def probar_editar_datos_de_un_proveedor_existente(self, id_proveedor_editar):
        found = resolve('/' + id_proveedor_editar + '/editar')
        self.assertEqual(found.func, editar_proveedor)

    def probar_que_el_titulo_de_la_lista_de_los_proveedores_sea_la_correcta(self):
        request = HttpRequest()
        response = nuevo_proveedor(request)
        self.assertTrue(response.content.contains('Lista proveedores'))
