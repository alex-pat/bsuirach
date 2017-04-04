from django.conf.urls import include, url
from . import views

app_name = 'employees'

urlpatterns = [
    url(r'^(?P<employee_id>[0-9]+)/$', views.show, name='show'),
    url(r'^update/$', views.update, name='update'),
    url(r'^(?P<employee_id>[0-9]+)/add_tags/$', views.add_tags, name='tags_add'),
    url(r'^(?P<employee_id>[0-9]+)/add_meme/$', views.add_meme, name='meme_add'),
]
