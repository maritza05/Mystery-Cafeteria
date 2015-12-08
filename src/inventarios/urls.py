from django.conf.urls import url
from inventarios.views import listar, modificar_inventario

urlpatterns = [
    url(r'^$', listar, name="listar"),
    url(r'^modificar/$', modificar_inventario, name="modificar_inventario"),
]