from django.urls import path

from myapp1.views import *

urlpatterns = [
    path('home/', home),
    path('home/user/' , user),
    path('home/user/<str:name>/' , shubham , name = "userName"),
    path('home/user/<str:name>/<str:login_emailid>/', shubham_login, name="userlogin"),
    path('home/user2/' , user2),
    path('home/user2/<str:name>/' , onkar , name = "userName"),
    path('home/user2/onkar/<str:name>/<str:login_emailid>' , onkar_login , name = "userlogin"),
]
