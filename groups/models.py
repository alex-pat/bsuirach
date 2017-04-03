from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    number = models.CharField(max_length=6)
    users = models.ManyToManyField(User)
