from django.db import models
from images.models import Image
from taggit.managers import TaggableManager

class Employee(models.Model):
    academicDepartment = models.CharField(max_length=100)
    calendarId = models.CharField(max_length=250)
    firstName = models.CharField(max_length=100)
    bsuir_id = models.IntegerField()
    lastName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100)
    photoLink = models.URLField(max_length=250)
    description = models.TextField()
    images = models.ManyToManyField(Image)
    tags = TaggableManager()

    _memes = models.TextField(blank=True)

    @property
    def memes(self):
        memes = self._memes.split('\n')
        return list(filter(bool, memes))

    @memes.setter
    def memes(self, value):
        self._memes = '\n'.join(filter(lambda x: x.strip(), value))

    def __str__(self):
        return "Employee {}: {} {}".format(
            self.pk,
            self.firstName,
            self.lastName
        )
