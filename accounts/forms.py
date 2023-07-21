from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import CustomUser


class UserRegForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'phone', 'user_type', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': 'true',
                                            'pattern': '[0-9]{6,12}',
                                            'title': 'Phone number should be 6-12 digits'}),
            'user_type': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'password1': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'password2': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
        }


class UserEditForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'is_active', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input m-2'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]{6,11}',
                                            'title': 'Phone number should be 6-11 digits'})
        }