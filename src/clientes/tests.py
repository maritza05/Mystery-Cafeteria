from django.test import TestCase
from django.core.urlresolvers import resolve
from clientes.views import listar, nuevo_cliente, eliminar_cliente, modificar_cliente, consulta_cliente
from django.http import HttpRequest


class ClientesTest(TestCase):

    def test_url_de_listar_clientes(self):
        found = resolve('/')
        self.assertEqual(found.func, listar)

    def test_titulo_de_la_lista_clientes(self):
        request = HttpRequest()
        response = nuevo_cliente(request)
        self.assertTrue(response.content.contains('Lista Clientes'))

    def test_url_agregar_nuevo_cliente(self):
        found = resolve('/nuevo')
        self.assertEqual(found.func, nuevo_cliente)

    def test_titulo_de_agregar_clientes(self):
        request = HttpRequest()
        response = nuevo_cliente(request)
        self.assertTrue(response.content.contains('Agregar Cliente'))


    def test_url_editar_cliente_(self, id_editar_cliente):
        found = resolve('/' + id_editar_cliente + '/modificar')
        self.assertEqual(found.func, editar_cliente)

    def test_titulo_de_modificar_clientes(self):
        request = HttpRequest()
        response = nuevo_cliente(request)
        self.assertTrue(response.content.contains('Modificar Cliente'))


    def test_url_eliminar_cliente(self, id_eliminar_cliente):
        found = resolve('/' + id_eliminar_cliente + '/eliminar')
        self.assertEqual(found.func, eliminar_cliente)
