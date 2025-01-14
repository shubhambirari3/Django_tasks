from django.urls import path
from HomeTwo.views import *

urlpatterns = [
    path('dashboard/', dashboard ,name='dashboard'),
    path('profile/', profile , name='profile'),
    path('settings/', settings),
    path('notifications/', notifications),
    path('logout/', logout),
]
