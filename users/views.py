from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from groups import bsuir_schedule


def show(request, username):
    user = get_object_or_404(User, username=username)
    groups = user.group_set.all()
    context = {
        'user': user,
        'username': request.user,
        'schedule': bsuir_schedule.html(
            groups[0].schedule
        ) if len(groups) > 0 else ''
    }
    return render(request, 'users/show.html', context)


def edit(request, username):
    user = request.user
    if username != user.username:
        return redirect("/")
    return render(request, 'users/edit.html', {'user': user, 'username': username})

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
