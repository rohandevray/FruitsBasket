from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
 

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['first_name','email','username','password1','password2']
        labels ={
            'first_name' : 'Name', #change the first name to name
        }

class CustomProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','short_intro','location','profile_image']
        labels={
            'profile_image':'Image',
            'short_intro':'Intro',
        }
