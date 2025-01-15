


from django.contrib import admin
from django.urls import path , include
from home.views import home_view , about  , proj_template

urlpatterns = [   
    path('home/', home_view),  
    path('home/hello/', about),  
    path('admin/', admin.site.urls),
    path('template_proj/' , proj_template ),
    path('tamplate_home/' , include('home.urls')) 
]
