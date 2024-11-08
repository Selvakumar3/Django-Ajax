import email
from django import forms
from django.contrib.auth.models import User
from .models import Details
from django.contrib.auth.models import UsercreationForm


class NewuserForm(UsercreationForm):
    email = forms.EmailField(required=True) 
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']