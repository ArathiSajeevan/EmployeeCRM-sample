from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from employees.forms import EmployeeForm, EmployeeEditForm
from employees.models import Employee

# Create your views here.


@login_required
def employee_add(request):
    form = EmployeeForm()
    template_name = "employees/employee_add.html"
    context = {'form': form}
    if request.method == "POST":
        form = EmployeeForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            print(data)
            messages.success(request, 'Employee Added Successfully.', 'alert-success')
            return redirect('employee_list')
        else:
            context = {'form': form}
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)
    

@login_required
def employee_list(request):
    mydata = Employee.objects.all()
    if(mydata != ''):
        return render(request, 'employees/employee_list.html',{'datas':mydata})
    else:
        return render(request, 'employees/employee_list.html')
    


@login_required()
def delete_employee(request, id):
    pk = request.GET.get("designation_id")
    Employee.objects.get(employee_id=id).delete()
    messages.success(request, 'Data Deleted Successfully.', 'alert-danger')
    return redirect('employee_list')

@login_required
def employee_edit(request, pk):
    template_name = "employees/employee_edit.html"
    employeeData = Employee.objects.get(employee_id = pk)
    form = EmployeeEditForm(instance=employeeData)
    

    if employeeData:
        editing = 1
    else:
        editing = 0

    context = {'form': form, 'DesignationForm':EmployeeForm, 'editing': editing}
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employeeData)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Employee Details Updated.', 'alert-success')
            return redirect('employee_list')
        else:
            context = {'form': form, 'editing': editing}
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)