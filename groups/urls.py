from django.conf.urls import include, url
from . import views

app_name = 'groups'

urlpatterns = [
    url(r'^update/$', views.update, name='update'),
    url(r'^(?P<number>\w+)/$', views.show, name='show'),
    url(r'^$', views.index, name='index'),
]
