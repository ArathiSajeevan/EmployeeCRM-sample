from django import forms
from master.models import department_model


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = department_model
        fields = ['department_id','department_name', 'description']

    department_id = forms.IntegerField(label="Department Id")
    department_name  = forms.CharField(label="Department Name", max_length=50)
    description = forms.Textarea()
