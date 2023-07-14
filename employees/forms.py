from django.forms import ModelForm
from django import forms
from .models import *
from employees.models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'employee_no', 'join_date', 'emp_start_date', 'emp_end_date', 'phone', 'address', 
                  'image', 'department_name','location_name', 'designation_name', 'status', 'skills' ]
        widget = {
            "name": forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
            "employee_no": forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
            "join_date" : forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "emp_start_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "emp_end_date" : forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control", 'required': 'true',
                                            'pattern': '[0-9]{6,12}',
                                            'title': 'Phone number should be 6-12 digits'
                                            }),
            "address": forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
            "image": forms.FileInput(attrs={'class': 'form-control'}),
            "department_name": forms.Select(attrs={"class": "form-control", "required": "true"}),
            "location_name": forms.Select(attrs={"class": "form-control", "required": "true"}),
            "designation_name": forms.Select(attrs={"class": "form-control", "required": "true"}),
            "status": forms.Select(attrs={'class': 'form-control'}),
            "skills" : forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),

        }


class EmployeeEditForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'employee_no', 'join_date', 'emp_start_date', 'emp_end_date', 'phone', 'address', 
                  'image', 'department_name','location_name', 'designation_name', 'status', 'skills' ]
        widget = {
            "name": forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
            "employee_no": forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
            "join_date" : forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "emp_start_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "emp_end_date" : forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control", 'required': 'true',
                                            'pattern': '[0-9]{6,12}',
                                            'title': 'Phone number should be 6-12 digits'
                                            }),
            "address": forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
            "image": forms.FileInput(attrs={'class': 'form-control'}),
            "department_name": forms.Select(attrs={"class": "form-control", "required": "true"}),
            "location_name": forms.Select(attrs={"class": "form-control", "required": "true"}),
            "designation_name": forms.Select(attrs={"class": "form-control", "required": "true"}),
            "status": forms.Select(attrs={'class': 'form-control'}),
            "skills" : forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),

        }
    
