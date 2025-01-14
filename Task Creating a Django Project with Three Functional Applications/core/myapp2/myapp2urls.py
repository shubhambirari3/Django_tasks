
from django.urls import path 
from .views import *

urlpatterns = [
    path('main/', main_page),
    path('about/<str:user_name>/', about_us , name='aboutUser'),
    path('contact/<int:contact>/', contact_us , name='contactUser'),
    path('services/', services),
    path('faq/', faq),
]
