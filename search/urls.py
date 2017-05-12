from django.conf.urls import include, url
from . import views

app_name = 'search'

urlpatterns = [
    url(r'^employees/$', views.employees, name='employees'),
    url(r'^users/$', views.users, name='users'),
    url(r'^comments/$', views.comments, name='comments'),
    url(r'^tags/$', views.tags, name='tags'),
]
