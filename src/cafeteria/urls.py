from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'cafeteria.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'cafeteria_administration.views.index', name='index'),
    url(r'cafeteria/', 'cafeteria_administration.views.cafeteria', name='cafeteria'),
    url(r'^admin/', include(admin.site.urls)),
]
