from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.settings import STATIC_URL
from .views import *

urlpatterns = [

    path('employee_add/', employee_add, name="employee_add"),
    path('employee_list/', employee_list, name="employee_list"),
    path('delete_employee/<str:id>', delete_employee, name="delete_employee"),
    path('employee_edit/<str:pk>', employee_edit, name="employee_edit"),
    path('employee_details/<str:pk>', employee_details.as_view(), name='employee_details'),
]
