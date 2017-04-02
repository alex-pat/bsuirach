from django.db import models

from cloudinary.models import CloudinaryField

class Image(models.Model):
    image = CloudinaryField('image')

    def __str__(self):
        return "Image {}".format(self.pk)
