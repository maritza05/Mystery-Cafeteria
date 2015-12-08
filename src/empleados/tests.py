from django.test import TestCase
from django.core.urlresolvers import resolve
from empleados.views import listar, nuevo_empleado, eliminar_empleado, modificar_empleado, consulta_empleado
from django.http import HttpRequest


class EmpleadosTest(TestCase):

    def test_url_de_listar_empleado(self):
        found = resolve('/')
        self.assertEqual(found.func, listar)

    def test_titulo_de_la_lista_empleado(self):
        request = HttpRequest()
        response = nuevo_empleado(request)
        self.assertTrue(response.content.contains('Lista Empleados'))

    def test_url_agregar_nuevo_empleado(self):
        found = resolve('/nuevo')
        self.assertEqual(found.func, nuevo_empleado)

    def test_titulo_de_agregar_empleado(self):
        request = HttpRequest()
        response = nuevo_empleado(request)
        self.assertTrue(response.content.contains('Agregar Empleado'))


    def test_url_editar_empleado_(self, id_editar_empleado):
        found = resolve('/' + id_editar_empleado + '/modificar')
        self.assertEqual(found.func, editar_empleado)

    def test_titulo_de_modificar_empleado(self):
        request = HttpRequest()
        response = modificar_empleado(request)
        self.assertTrue(response.content.contains('Modificar Empleado'))


    def test_url_eliminar_empleado(self, id_eliminar_empleado):
        found = resolve('/' + id_eliminar_empleado + '/eliminar')
        self.assertEqual(found.func, eliminar_empleado)
