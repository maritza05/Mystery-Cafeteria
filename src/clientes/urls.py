from django.conf.urls import url
from clientes.views import listar, nuevo_cliente, eliminar_cliente, modificar_cliente, consultar_cliente


urlpatterns = [
    url(r'^$', listar, name="listar"),
    url(r'^nuevo/$', nuevo_cliente, name="nuevo_cliente"),
    url(r'^(?P<pk>[0-9]+)/modificar', modificar_cliente, name="modificar_cliente"),
    url(r'^(?P<pk>[0-9]+)/eliminar', eliminar_cliente, name="eliminar_cliente"),
     url(r'^(?P<pk>[0-9]+)/consultar', consultar_cliente, name="consultar_cliente"),
]
