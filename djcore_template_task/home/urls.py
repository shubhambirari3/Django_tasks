from django.urls import path 

from .views import template_sample

urlpatterns = [
    path('template_sample/', template_sample)
]