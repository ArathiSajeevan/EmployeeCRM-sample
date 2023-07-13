from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.settings import STATIC_URL
from .views import *

urlpatterns = [

    path('employee_add/', employee_add, name="employee_add"),
    path('employee_list/', employee_list, name="employee_list"),
]
