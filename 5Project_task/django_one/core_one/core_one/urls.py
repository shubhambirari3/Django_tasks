"""
URL configuration for core_one project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from Home_one.views import home  #insted of importing all function use * to import all methods from views.py
from Home_one.views import *

urlpatterns = [
    path('home/', home),
    path('home/user/' , user),
    path('home/user/shubham/' , shubham),
    path('home/user/shubham/login/' , shubham_login),
    path('home/user2/' , user2),
    path('home/user2/onkar/' , onkar),
    path('home/user2/onkar/login/' , onkar_login),
]
