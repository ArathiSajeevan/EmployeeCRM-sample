from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',login_user,name="login"),
    path('user_reg', sign_up, name='user_reg'),
    path('user_list', Userlist.as_view(), name='user_list'),
]