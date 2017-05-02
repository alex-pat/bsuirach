from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Image(models.Model):
    image = CloudinaryField('image')
    user = models.OneToOneField(User, null=True)

    def __str__(self):
        return "Image {}".format(self.pk)
