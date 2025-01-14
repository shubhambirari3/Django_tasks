from django.shortcuts import render, HttpResponse

# Create your views here.

def dashboard(request):
    return HttpResponse("Welcome to the Dashboard of Project One!")

def profile(request):
    return HttpResponse("This is the Profile page of Project One!")

def settings(request):
    return HttpResponse("This is the Settings page of Project One!")

def notifications(request):
    return HttpResponse("Here are your Notifications for Project One!")

def logout(request):
    return HttpResponse("You have been logged out of Project One!")
