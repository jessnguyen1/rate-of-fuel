from django.contrib.auth.forms import UserCreationForm
from django import forms
from . models import UserProfileModel
from django.forms import ModelForm


class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfileModel
        fields = '__all__'

