from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from gallery.models import Image


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['Original_Image']


class UpdateColoringPageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['sigma']
