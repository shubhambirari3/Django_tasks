


from django.contrib import admin
from django.urls import path , include
from home.views import *

urlpatterns = [   
    path('template_emplo/' , employee_details ),
    path('template_proj/' , proj_template ),
    path('tamplate_home/' , include('home.urls'))           
]
