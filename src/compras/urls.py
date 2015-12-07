from django.conf.urls import url
from compras.views import listar, nueva_compra, eliminar_compra, menu_productos, promociones

urlpatterns = [
    url(r'^$', listar, name="listar"),
    url(r'^nuevo/$', nueva_compra, name="nueva_compra"),
    url(r'^(?P<pk>[0-9]+)/eliminar', eliminar_compra, name="eliminar_compra"),
    url(r'^menu/', menu_productos, name="menu_productos"),
    url(r'^promociones/', promociones, name="promociones"),
]
