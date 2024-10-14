# users/forms.py

from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email', 'address']  # Only use fields that exist in your model
