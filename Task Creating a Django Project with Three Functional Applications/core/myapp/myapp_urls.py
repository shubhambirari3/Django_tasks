from django.urls import path
from myapp.views import *

urlpatterns = [
    path('dashboard/', dashboard ,name='dashboard'),
    path('profile/', profile , name='profile'),
    path('settings/', settings),
    path('notifications/', notifications),
    path('logout/', logout),
]
