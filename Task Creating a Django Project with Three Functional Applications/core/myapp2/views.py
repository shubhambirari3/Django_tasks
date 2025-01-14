from django.shortcuts import render, HttpResponse

# Create your views here.

def main_page(request):
    return HttpResponse("Welcome to the Main Page of Project Two!")

def about_us(request , user_name):
    return HttpResponse(f"Learn more About {user_name} on this page of Project Two!")

def contact_us(request , contact):
    return HttpResponse(f"Contact on {contact} Us via this page in Project Two!")

def services(request):
    return HttpResponse("Here are the Services we offer from homeThree!")

def faq(request):
    return HttpResponse("Frequently Asked Questions for Project Two!")
