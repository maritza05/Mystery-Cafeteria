from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'cafeteria.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('cafeteria_administration.urls'), name='index'),
    url(r'cafeteria/', include('cafeteria_administration.urls'), name='cafeteria'),
    url(r'^admin/', include(admin.site.urls)),
]
