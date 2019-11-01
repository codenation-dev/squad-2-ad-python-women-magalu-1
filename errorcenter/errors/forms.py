from django import forms
from django.db import models

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__' 