from django import forms
from django.forms import ModelForm
from images.models import Image

class ImageForm(ModelForm):
    class Meta:
        model = Image
        exclude = ['user']
