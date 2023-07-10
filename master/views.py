from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control

from master.forms import DepartmentEditForm
from .models import tbl_department
from master.forms import DepartmentForm
from django.contrib import messages

# Create your views here.

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    return render(request, 'master/dashboard.html')


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def department(request):
    form = DepartmentForm()
    template_name = "master/department.html"
    context = {'form': form}
    if request.method == "POST":
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'department Successfully Added.', 'alert-success')
            return redirect('view_department_details')
        else:
            context = {'form': form}
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)




def admin_logout(request):
    logout(request)
    return redirect('/')


@login_required()
def delete_depData(request, id):
    pk = request.GET.get("department_id")
    tbl_department.objects.get(department_id=id).delete()
    messages.success(request, 'Data Deleted Successfully.', 'alert-danger')
    return redirect('view_department_details')


#######

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def view_department_details(request):
    mydata = tbl_department.objects.all()
    if(mydata != ''):
        return render(request, 'master/view_department_details.html',{'datas':mydata})
    else:
        return render(request, 'master/view_department_details.html')
    


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_dep_view(request, pk):
    template_name = "master/update_dep_view.html"
    departmentData = tbl_department.objects.get(department_id = pk)
    form = DepartmentEditForm(instance=departmentData)
    

    if departmentData:
        editing = 1
    else:
        editing = 0

    context = {'form': form, 'DepartmentForm':DepartmentForm, 'editing': editing}
    if request.method == "POST":
        form = DepartmentForm(request.POST, request.FILES, instance=departmentData)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Department Details Updated.', 'alert-success')
            return redirect('view_department_details')
        else:
            context = {'form': form, 'editing': editing}
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)
######
    






