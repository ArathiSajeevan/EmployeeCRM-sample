from django.forms import ModelForm
from django import forms
from .models import *


class DepartmentForm(ModelForm):
    class Meta:
        model = tbl_department
        fields = ['department_name', 'description']

        widgets = {
            "department_name":forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
            "description":forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
        }

class DepartmentEditForm(ModelForm):
    class Meta:
        model = tbl_department
        fields = ['department_name', 'description']

        widgets = {
            "department_name":forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
            "description":forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
        }
