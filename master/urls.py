from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.settings import STATIC_URL
from .views import *

urlpatterns = [
    path('admin_logout',admin_logout,name="admin_logout"),

    #department
    path('dashboard/', dashboard, name="dashboard"),
    path('department/', department, name='department'),
    path('view_department_details', view_department_details, name="view_department_details"),
    path('update_dep_view/<str:pk>', update_dep_view, name="update_dep_view"),
    path('delete_depData/<str:id>', delete_depData, name="delete_depData"),
    


    #designation
    path('designation_add', designation_add, name='designation_add'),
    path('designation_list', designation_list, name='designation_list'),
    path('update_designation/<str:pk>', update_designation, name="update_designation"),
    path('delete_designation/<str:id>', delete_designation, name="delete_designation"),


    #location
    path('location_add', location_add, name="location_add"),
    path('location_list', location_list, name="location_list"),
    path('update_location/<str:pk>', update_location, name="update_location"),

]
