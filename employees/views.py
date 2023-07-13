from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from employees.forms import EmployeeForm

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
            messages.success(request, 'Employee Successfully Added.', 'alert-success')
            return redirect('employee_add')
        else:
            context = {'form': form}
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)
    