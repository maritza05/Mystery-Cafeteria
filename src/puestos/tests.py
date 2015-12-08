from django.test import TestCase
from django.core.urlresolvers import resolve
from puestos.views import listar, nuevo_puesto, eliminar_puesto, modificar_puesto, consulta_puesto
from django.http import HttpRequest


class PuestoTest(TestCase):

    def test_url_de_listar_puesto(self):
        found = resolve('/')
        self.assertEqual(found.func, listar)

    def test_titulo_de_la_lista_puesto(self):
        request = HttpRequest()
        response = nuevo_puesto(request)
        self.assertTrue(response.content.contains('Lista Puestos'))

    def test_url_agregar_nuevo_puesto(self):
        found = resolve('/nuevo')
        self.assertEqual(found.func, nuevo_puesto)

    def test_titulo_de_agregar_puesto(self):
        request = HttpRequest()
        response = nuevo_puesto(request)
        self.assertTrue(response.content.contains('Agregar Puesto'))


    def test_url_editar_puesto_(self, id_editar_puesto):
        found = resolve('/' + id_editar_puesto + '/modificar')
        self.assertEqual(found.func, editar_puesto)

    def test_titulo_de_modificar_puesto(self):
        request = HttpRequest()
        response = nuevo_puesto(request)
        self.assertTrue(response.content.contains('Modificar Puesto'))


    def test_url_eliminar_puesto(self, id_eliminar_puesto):
        found = resolve('/' + id_eliminar_puesto + '/eliminar')
        self.assertEqual(found.func, eliminar_puesto)
