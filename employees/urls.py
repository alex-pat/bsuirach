from django.conf.urls import include, url
from . import views

app_name = 'employees'

urlpatterns = [
    url(r'^(?P<employee_id>[0-9]+)/$', views.show, name='show'),
]
