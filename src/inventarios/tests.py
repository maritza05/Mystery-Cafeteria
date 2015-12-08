from django.test import TestCase
from django.core.urlresolvers import resolve
from inventarios.views import listar, modificar_inventario
from django.http import HttpRequest


class PuestoTest(TestCase):

    def test_url_de_listar_inventario(self):
        found = resolve('/')
        self.assertEqual(found.func, listar)

    def test_titulo_de_la_lista_inventario(self):
        request = HttpRequest()
        response = lista_inventario(request)
        self.assertTrue(response.content.contains('Lista Inventarios'))

    def test_titulo_de_modificar_cantidad(self):
        request = HttpRequest()
        response = modificar_inventario(request)
        self.assertTrue(response.content.contains('Modificar Inventario'))


    def test_url_modificar_inventario(self, id_eliminar_puesto):
        found = resolve('/' + id_producto + '/modificar_inventario')
        self.assertEqual(found.func, modificar_inventario)

# Create your tests here.
