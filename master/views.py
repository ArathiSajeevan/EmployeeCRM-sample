from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control
from .models import department_model
from master.forms import DepartmentForm

# Create your views here.

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    return render(request, 'master/dashboard.html')


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def department(request):
    context = {}
    context['form'] = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES)

        if form.is_valid():
            departmentdatas = department_model(
                department_id=form.cleaned_data['department_id'], 
                department_name=form.cleaned_data['department_name'], 
                description=form.cleaned_data['description'], 
                
                )
            departmentdatas.save()
            form = DepartmentForm()
            return render(request, "master/department.html",{
                "form" : form
            })
    
    else:
        form = DepartmentForm()
        return render(request, 'master/department.html',{
            "form" : form
    })


def admin_logout(request):
    logout(request)
    return redirect('/')




