from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.settings import STATIC_URL
from .views import *

urlpatterns = [
    path('admin_logout',admin_logout,name="admin_logout"),

    #master
    path('dashboard/', dashboard, name="dashboard"),
    path('view_department_details', view_department_details, name="view_department_details"),
    path('department/', department, name='department'),
    path('delete_depData/<str:id>', delete_depData, name="delete_depData"),
    path('update_dep_view/<str:pk>', update_dep_view, name="update_dep_view"),

]
