from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Group
from .bsuir_schedule import GroupScheduler, html_table


@user_passes_test(lambda u: u.is_superuser)
def update(request):
    scheduler = GroupScheduler()
    for group in Group.objects.all():
        group.schedule = scheduler.group(group.number)
        group.save()
    return HttpResponse("Success")


def index(request):
    context = {
        'username': request.user.username,
        'groups': Group.objects.all(),
    }
    return render(request, 'groups/index.html', context)


def show(request, number):
    group = get_object_or_404(Group, number=number)
    context = {
        'username': request.user.username,
        'group': group,
        'schedule': html_table(group.schedule),
    }
    return render(request, 'groups/show.html', context)
