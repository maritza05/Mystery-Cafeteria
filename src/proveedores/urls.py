from django.conf.urls import url
from proveedores.views import listar, nuevo_proveedor, editar_proveedor, eliminar_proveedor

urlpatterns = [
    url(r'^$', listar, name="listar"),
    url(r'^nuevo/$', nuevo_proveedor, name='nuevo_proveedor'),
    url(r'^(?P<pk>[0-9]+)/eliminar', eliminar_proveedor, name="eliminar_proveedor"),
    url(r'^(?P<pk>[0-9]+)/editar', editar_proveedor, name="editar_proveedor"),
]
