from django.conf.urls import url
from empleados.views import listar, nuevo_empleado, eliminar_empleado, modificar_empleado, consulta_empleado


urlpatterns = [
    url(r'^$', listar, name="listar"),
    url(r'^nuevo/$', nuevo_empleado, name="nuevo_empleado"),
    url(r'^(?P<pk>[0-9]+)/modificar', modificar_empleado, name="modificar_empleado"),
    url(r'^(?P<pk>[0-9]+)/eliminar', eliminar_empleado, name="eliminar_empleado"),
    url(r'^(?P<pk>[0-9]+)/consulta', consulta_empleado, name="consulta_empleado"),
]
