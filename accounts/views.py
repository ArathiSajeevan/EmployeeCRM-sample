from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def login_user(request):
    template_name = "accounts/login.html"
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        cus_user = User.objects.filter(username=username).exists()
        if cus_user:
            custome_user = User.objects.get(username=username)
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


