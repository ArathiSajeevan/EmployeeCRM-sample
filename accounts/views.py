from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.forms import UserRegForm
from employees.models import Employee
from accounts.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *

from accounts.forms import UserEditForm


# Create your views here.

def login_user(request):
    template_name = "accounts/login.html"
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        cus_user = CustomUser.objects.filter(username=username).exists()
        if cus_user:
            custome_user = CustomUser.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                context = {"msg":"Invalid Credentials"}
                return render(request,template_name,context=context)
        else:
            context = {"msg":"Incorrect Username"}
            return render(request, template_name, context=context)
    return render(request, template_name)


@login_required
def sign_up(request):
    if request.method == 'GET':
        form = UserRegForm
        context = {"form": form}
        return render(request, 'accounts/user_reg.html', context)
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            if data.user_type == "Viewer" or data.user_type == "Admin":
                name = data.first_name + " " + data.last_name
                Employee.objects.create(
                    created_user=str(request.user),
                    name=name,
                    status='Active',
                    phone=data.phone,
                
                )
        messages.success(request, 'New User Successfully Created', 'alert-success')
        return redirect('user_list')
    else:
        context = {'form': form}
        print(form.errors)
        messages.success(request, 'Invalid Data', 'alert-danger')
        return render(request, 'accounts/user_reg.html', context)



class Userlist(LoginRequiredMixin, TemplateView):
    template_name = "accounts/user_list.html"

    def get(self, request, *args, **kwargs):
        if request.user.user_type == "Admin":
            userlist = CustomUser.objects.all()
        else:
            userlist = CustomUser.objects.filter(id=request.user.id)
        context = {'userlist': userlist}
        return render(request, self.template_name, context)



@login_required()
def user_edit(request, pk):
    user = CustomUser.objects.get(id=pk)
    if user.user_type != "Viewer":
        emp = Employee.objects.get(emp_user=pk)
    form = UserEditForm(instance=user)
    template_name = "accounts/user_edit.html"
    context = {'form': form, 'user': user}
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        context = {'form': form, 'user': user}
        if form.is_valid():
            data = form.save(commit=False)
            if user.user_type != "Viewer":
                if data.is_active == True:
                    emp.status = "Active"
                else:
                    emp.status = "Inactive"
                    emp.save()
            data.save()
            messages.success(request, 'User Details Successfully Updated', 'alert-success')
            return redirect('user_list')
        else:
            messages.success(request, 'Invalid Data', 'alert-danger')
            return render(request, template_name, context)
    return render(request, template_name, context)