from django.conf.urls import include, url
from . import views

app_name = 'images'

urlpatterns = [
    url(r'^create/$', views.create, name='create'),
]
