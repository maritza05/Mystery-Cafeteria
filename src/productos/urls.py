from django.conf.urls import url
from productos.views import listaproductos, nuevo_producto, eliminar_producto, editar_producto

urlpatterns = [
    url(r'^$', listaproductos, name="listaproductos"),
    url(r'^nuevo/$', nuevo_producto, name="nuevo_producto"),
    url(r'^(?P<pk>+)/eliminar', eliminar_producto, name="eliminar_producto"),
    url(r'^(?P<pk>+)/editar', editar_producto, name="editar_producto"),
]