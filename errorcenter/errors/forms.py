from django import forms
from django.db import models

from .models import User

class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'nome'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'sobrenome'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'senha'}))
    class Meta:
        model = User
        exclude = (
                    'date_joined',
                    'is_staff',
                    'is_active',
                    'objects'
                )
        fields = '__all__' 
        