from django import forms
from django.forms import ModelForm

from employees.models import Employee

class EmployeeReportForm(forms.Form):
    emp_start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date', 'max': '4000-12-31', 'required': 'true'}))
    emp_end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date', 'max': '4000-12-31', 'required': 'true'}))
    
    def __init__(self, *args, **kwargs):
        super(EmployeeReportForm, self).__init__(*args, **kwargs)
        employee_choices = [(i.employee_id, i.name, i.emp_start_date, i.emp_end_date) for i in
                            Employee.objects.filter(status='Active')]
        employee_choices.insert(0, ('', 'All'))
        
        self.fields['employee'] = forms.ChoiceField(
            choices=employee_choices, widget=forms.Select(attrs={'class': 'form-control'}),
            required=False)
        



class EmployeeForm(forms.Form):
    class Meta:
        model = Employee
        fields = ['name', 'join_date', 'emp_start_date', 'emp_end_date', 'phone', 'address', 
                  'department_name','location_name', 'designation_name', 'status', 'skills' ]