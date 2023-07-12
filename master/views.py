from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control

from master.forms import DepartmentForm, DepartmentEditForm
from master.forms import DesignationForm, DesignationEditForm
from master.forms import LocationAddForm, LocationEditForm
from .models import Designation, tbl_department, Location
from django.contrib import messages

# Create your views here.

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    return render(request, 'master/dashboard.html')

#Department

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
        form = DepartmentForm(request.POST, instance=departmentData)
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


#Designation

@login_required
def designation_add(request):
    form = DesignationForm()
    template_name = "master/designation_add.html"
    context = {'form': form}
    if request.method == "POST":
        form = DesignationForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Designation Successfully Added.', 'alert-success')
            return redirect('designation_list')
        else:
            context = {'form': form}
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)
    

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def designation_list(request):
    mydata = Designation.objects.all()
    if(mydata != ''):
        return render(request, 'master/designation_list.html',{'datas':mydata})
    else:
        return render(request, 'master/designation_list.html')
    


@login_required()
def delete_designation(request, id):
    pk = request.GET.get("designation_id")
    Designation.objects.get(designation_id=id).delete()
    messages.success(request, 'Data Deleted Successfully.', 'alert-danger')
    return redirect('designation_list')



@login_required
def update_designation(request, pk):
    template_name = "master/update_designation.html"
    designationData = Designation.objects.get(designation_id = pk)
    form = DesignationEditForm(instance=designationData)
    

    if designationData:
        editing = 1
    else:
        editing = 0

    context = {'form': form, 'DesignationForm':DesignationForm, 'editing': editing}
    if request.method == "POST":
        form = DesignationForm(request.POST, instance=designationData)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Designation Details Updated.', 'alert-success')
            return redirect('designation_list')
        else:
            context = {'form': form, 'editing': editing}
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)



@login_required
def location_add(request):
    form = LocationAddForm()
    template_name = "master/location_add.html"
    context = {'form': form}
    if request.method == "POST":
        form = LocationAddForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Location Successfully Added.', 'alert-success')
            return redirect('location_add')
        else:
            context = {'form': form}
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)
    


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def location_list(request):
    mydata = Location.objects.all()
    if(mydata != ''):
        return render(request, 'master/location_list.html',{'datas':mydata})
    else:
        return render(request, 'master/location_list.html')




@login_required
def update_location(request, pk):
    template_name = "master/update_location.html"
    locationData = Location.objects.get(location_id = pk)
    form = LocationEditForm(instance=locationData)
    

    if locationData:
        editing = 1
    else:
        editing = 0

    context = {'form': form, 'LocationAddForm':LocationAddForm, 'editing': editing}
    if request.method == "POST":
        form = LocationAddForm(request.POST, instance=locationData)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Location Details Updated.', 'alert-success')
            return redirect('location_list')
        else:
            context = {'form': form, 'editing': editing}
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)
    

@login_required()
def delete_location(request, id):
    pk = request.GET.get("location_id")
    Location.objects.get(location_id=id).delete()
    messages.success(request, 'Data Deleted Successfully.', 'alert-danger')
    return redirect('location_list')