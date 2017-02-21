from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def show(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'show.html', {'user': user, 'username': user.username})
