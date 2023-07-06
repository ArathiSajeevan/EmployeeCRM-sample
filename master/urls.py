from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path('admin_logout',admin_logout,name="admin_logout"),

    #master
    # path('department/', department, name='department'),

]