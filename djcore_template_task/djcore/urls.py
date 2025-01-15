


from django.contrib import admin
from django.urls import path , include
from home.views import home_view , about  

urlpatterns = [   
    path('home/', home_view),  
    path('home/hello/', about),  
    path('admin/', admin.site.urls),
    path('tamplate_home/' , include('home.urls')) 
]
