from django.conf.urls import include, url
from . import views

app_name = 'images'

urlpatterns = [
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<username>[\w-]+)/set$', views.set_avatar, name='set_avatar'),
]
