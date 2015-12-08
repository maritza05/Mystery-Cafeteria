from django.test import TestCase
from django.core.urlresolvers import resolve
from productos.views import listaproductos, nuevo_producto, eliminar_producto, editar_producto
from django.http import HttpRequest
 
# Create your tests here.

class ProductoTest(TestCase):

    def probar_la_url_de_listaproductos(self):
        found = resolve('/')
        self.assertEqual(found.func, listaproductos)

    def probar_la_url_de_agregar_nuevo_producto(self):
        found = resolve('/nuevo_producto')
        self.assertEqual(found.func, nuevo_producto)

    def probar_la_url_de_eliminar_producto(self, nombre_producto):
        found = resolve('/' + nombre_producto + '/eliminar')
        self.assertEqual(found.func, eliminar_producto)

    def probar_si_listar_devuelve_los_datos_esperados(self):
        request = HttpRequest()
        response = listar(request)
        self.assertTrue(response.content.endswith('</html>'))

    def probar_editar_datos_de_un_producto_existente(self, nombre_producto):
        found = resolve('/' + nombre_producto + '/editar')
        self.assertEqual(found.func, editar_producto)

    def probar_que_el_titulo_de_la_lista_de_los_productos_sea_la_correcta(self):
        request = HttpRequest()
        response = nuevo_producto(request)
        self.assertTrue(response.content.contains('Lista productos'))