from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.settings import STATIC_URL
from .views import *

urlpatterns = [
    path('admin_logout',admin_logout,name="admin_logout"),

    #master
    path('', dashboard, name="dashboard"),
    path('department/', department, name='department'),

]
