from django import forms
from django.forms import ModelForm

from employees.models import Employee


class EmployeeReportForm(forms.Form):
    from_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date', 'max': '4000-12-31', 'required': 'true'}))
    to_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date', 'max': '4000-12-31', 'required': 'true'}))
    
    def __init__(self, *args, **kwargs):
        super(EmployeeReportForm, self).__init__(*args, **kwargs)
        employee_choices = [(i.employee_id, i.name) for i in
                            Employee.objects.filter(status='Active')]
        employee_choices.insert(0, ('', 'All'))
        self.fields['employee'] = forms.ChoiceField(
            choices=employee_choices, widget=forms.Select(attrs={'class': 'form-control'}),
            required=False)