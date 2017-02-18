from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.db import models

def index(request):
    return render_to_response('index.html', { 'username': auth.get_user(request).username})
