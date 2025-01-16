from django.urls import path 

from .views import student_template , template_sample , student_name

urlpatterns = [
    path('sample_temp/', template_sample),
    path('student_template/' , student_template),
    path('student_name/' , student_name)
]