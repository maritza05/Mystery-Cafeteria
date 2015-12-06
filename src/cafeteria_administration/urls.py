from django.conf.urls import url
from . import views 
urlpatterns = [
    url(r'^$', 'cafeteria_administration.views.index', name='index'),
    url(r'cafeteria/', 'cafeteria_administration.views.cafeteria', name='cafeteria'),
]