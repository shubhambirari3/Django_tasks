from django.shortcuts import render , HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("this is home page of proj core_one!!")

def user(request):
    return HttpResponse("this is user page of proj core_one!!")

def shubham(request , name):
    return HttpResponse(f"this is ,{name} page of proj core_one!!")

def shubham_login(request, name, login_emailid):
    return HttpResponse(f"Login page for user {name} with email id: {login_emailid}")

def user2(request):
    return HttpResponse("this is user2 page of proj core_one!!")

def onkar(request, name,):
    return HttpResponse(f"this is {name} page of proj core_one!!")

def onkar_login(request,name , login_emailid):
    return HttpResponse(f"Login page for user {name} with email id : {login_emailid}")

