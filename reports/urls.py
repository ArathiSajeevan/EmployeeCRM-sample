from django.urls import path
from .views import *

urlpatterns = [
    path('employee_reports', employee_reports, name='employee_reports'),
]