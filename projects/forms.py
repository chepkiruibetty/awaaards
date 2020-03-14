from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image','title','desc','link']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]

        