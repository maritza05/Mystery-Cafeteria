from django.conf.urls import url
from compras.views import listar, nueva_compra, eliminar_compra, detalles_compra

urlpatterns = [
    url(r'^$', listar, name="listar"),
    url(r'^nuevo/$', nueva_compra, name="nueva_compra"),
    url(r'^(?P<pk>[0-9]+)/detalles', detalles_compra, name="detalles_compra"),
    url(r'^(?P<pk>[0-9]+)/eliminar', eliminar_compra, name="eliminar_compra"),
]
