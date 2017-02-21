from django.conf.urls import include, url
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^(?P<username>\w+)/$', views.show, name='show'),
]
