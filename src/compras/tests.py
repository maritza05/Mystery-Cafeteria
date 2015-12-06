from django.test import TestCase
from django.core.urlresolvers import resolve
from compras.views import listar, nueva_compra, eliminar_compra
from django.http import HttpRequest


class ComprasTest(TestCase):

    def probar_la_url_de_listar_las_compras(self):
        found = resolve('/')
        self.assertEqual(found.func, listar)

    def probar_la_url_de_crear_una_nueva_compra(self):
        found = resolve('/nueva_compra')
        self.assertEqual(found.func, nueva_compra)

    def probar_la_url_de_eliminar_una_compra(self, id_compra_eliminar):
        found = resolve('/' + id_compra_eliminar + '/eliminar')
        self.assertEqual(found.func, eliminar_compra)

    def probar_si_listar_devuelve_los_datos_esperados(self):
        request = HttpRequest()
        response = listar(request)
        self.assertTrue(response.content.endswith('</html>'))
