from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# This function handles requests to the "home" URL
def home_view(request):
    return HttpResponse("Welcome to my Django app!")

def about(request):
    return HttpResponse("Hello, Subhs!")    


def template_sample(request):
    return render(request, 'index.html') 

def proj_template(request):
    return render(request, 'proj_index.html')