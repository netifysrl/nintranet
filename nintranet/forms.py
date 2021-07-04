from typing import Text
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import TextInput


class DetailUserForm(forms.ModelForm):
    
    name = forms.CharField(widget=TextInput())
    lastname = forms.CharField(widget=TextInput())
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    conferma_password = forms.CharField(widget=forms.PasswordInput())
    
    
    class Meta:
        model = User
        fields = ["username", "email", "password", "nome", "cognome",]


