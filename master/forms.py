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
            "description": forms.Textarea(attrs={"class": "form-control", 'rows': 3})
        }

class DesignationForm(ModelForm):
    class Meta:
        model = Designation
        fields = ['department_name', 'designation_name', 'description']
        widgets = {
            "department_name": forms.Select(attrs={"class": "form-control", 'required': 'true'}),
            "designation_name": forms.TextInput(attrs={"class":"form-control", 'required':'true'}),
            "description": forms.Textarea(attrs={"class": "form-control", 'rows': 3})
        }

class DesignationEditForm(ModelForm):
    class Meta:
        model = Designation
        fields = ['department_name', 'designation_name', 'description']
        widgets = {
            "department_name": forms.Select(attrs={"class": "form-control", 'required': 'true'}),
            "designation_name": forms.TextInput(attrs={"class":"form-control", 'required':'true'}),
            "description": forms.Textarea(attrs={"class": "form-control", 'rows': 3})
        }

class LocationAddForm(ModelForm):
    class Meta:
        model = Location
        fields = ['location_name', 'description']
        widgets = {
            "location_name": forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
            "description": forms.Textarea(attrs={"class": "form-control", 'rows': 2})
        }

class LocationEditForm(ModelForm):
    class Meta:
        model = Location
        fields = ['location_name', 'description']
        widgets = {
            "location_name": forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
            "description": forms.Textarea(attrs={"class": "form-control", 'rows': 2})
        }