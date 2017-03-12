from django.db import models


class Employee(models.Model):
    academicDepartment = models.CharField(max_length=100)
    calendarId = models.CharField(max_length=250)
    firstName = models.CharField(max_length=100)
    bsuir_id = models.IntegerField()
    lastName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100)
    photoLink = models.URLField(max_length=250)
    description = models.TextField()
