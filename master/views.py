from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control

# Create your views here.

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    return render(request, 'master/dashboard.html')


def admin_logout(request):
    logout(request)
    return redirect('/')




