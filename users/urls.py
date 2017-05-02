from django.conf.urls import include, url
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', views.show, name='show'),
    url(r'^(?P<username>[\w-]+)/edit$', views.edit, name='edit'),
    url(r'^(?P<username>[\w-]+)/update$', views.update, name='update'),
]
