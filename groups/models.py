from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    number = models.CharField(max_length=6)
    users = models.ManyToManyField(User)
    raw_schedule = models.TextField(blank=True)

    @property
    def schedule(self):
        return eval(self.raw_schedule)

    @schedule.setter
    def schedule(self, value):
        self.raw_schedule = repr(value)

    def __str__(self):
        return self.number
