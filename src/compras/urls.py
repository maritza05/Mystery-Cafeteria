from django.conf.urls import url
from compras.views import listar

urlpatterns = [
    url(r'^$', listar, name="listar"),
]
