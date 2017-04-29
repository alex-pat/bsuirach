from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Group
from .bsuir_schedule import GroupScheduler


@user_passes_test(lambda u: u.is_superuser)
def update(request):
    scheduler = GroupScheduler()
    for group in Group.objects.all():
        group.schedule = scheduler.group(group.number)
        group.save()
    return HttpResponse("Success")
