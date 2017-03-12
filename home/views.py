from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.db import models
from employees.models import Employee

def index(request):
    employees = Employee.objects.all()
    return render_to_response('home/index.html', {'employees': employees, 'username': auth.get_user(request).username})
