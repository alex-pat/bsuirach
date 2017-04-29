from django.conf.urls import include, url
from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^update/$', views.update, name='update'),
]
