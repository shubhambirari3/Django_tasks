from django.shortcuts import render , HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("this is home page of proj core_one!!")

def user(request):
    return HttpResponse("this is user page of proj core_one!!")

def shubham(request):
    return HttpResponse("this is shubham page of proj core_one!!")

def shubham_login(request):
    return HttpResponse("login page for user name shubham of proj core_one!!")

def user2(request):
    return HttpResponse("this is user2 page of proj core_one!!")

def onkar(request):
    return HttpResponse("this is onkar page of proj core_one!!")

def onkar_login(request):
    return HttpResponse("login page for user name onkar of proj core_one!!")

