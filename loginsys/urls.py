from django.conf.urls import include, url
from . import views

app_name = 'loginsys'

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register),
]
