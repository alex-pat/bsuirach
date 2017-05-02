from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.db import models
from employees.models import Employee
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    employees = Employee.objects.order_by('lastName')
    return render_to_response('home/index.html', {
        'employees': employees,
        'username': auth.get_user(request).username
    })
