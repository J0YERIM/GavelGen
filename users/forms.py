from django import forms
from .models import User


class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
