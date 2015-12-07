from django.conf.urls import url
from clientes.views import listar, nuevo_cliente, eliminar_cliente, modificar_clientes

urlpatterns = [
    url(r'^$', listar, name="listar"),
    url(r'^nuevo/$', nuevo_cliente, name="nueva_cliente"),
    url(r'^(?P<pk>[0-9]+)/modificar', modificar_clientes, name="modificar_clientes "),
    url(r'^(?P<pk>[0-9]+)/eliminar', eliminar_compra, name="eliminar_cliente"),
]
