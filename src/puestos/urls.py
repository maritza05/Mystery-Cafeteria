from django.conf.urls import url
from puestos.views import listar, nuevo_puesto, eliminar_puesto, modificar_puesto, consulta_puesto


urlpatterns = [
    url(r'^$', listar, name="listar"),
    url(r'^nuevo/$', nuevo_puesto, name="nuevo_puesto"),
    url(r'^(?P<pk>[0-9]+)/modificar', modificar_puesto, name="modificar_puesto"),
    url(r'^(?P<pk>[0-9]+)/eliminar', eliminar_puesto, name="eliminar_puesto"),
    url(r'^(?P<pk>[0-9]+)/consulta', consulta_puesto, name="consulta_puesto"),
]
