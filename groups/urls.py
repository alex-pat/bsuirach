from django.conf.urls import include, url
from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^update/$', views.update, name='update'),
    url(r'^$', views.index, name='index'),
]
