from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User


def show(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'show.html', {'user': user, 'username': request.user})


def edit(request, username):
    user = request.user
    if username != user.username:
        return redirect("/")
    return render(request, 'edit.html', {'user': user, 'username': username})

def update(request, username):
    user = request.user
    if username != user.username:
        return
    user.username = request.POST['username']
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/users/' + user.username)
