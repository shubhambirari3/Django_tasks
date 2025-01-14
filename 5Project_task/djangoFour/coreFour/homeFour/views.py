from django.shortcuts import render, HttpResponse

# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to the Welcome Page of Project Three!")

def products(request):
    return HttpResponse("Explore our range of Products in Project Three!")

def product_detail(request):
    return HttpResponse("Here you can find details about a specific product.")

def cart(request):
    return HttpResponse("Your Shopping Cart is ready for checkout in Project Three!")

def payment(request):
    return HttpResponse("Proceed with Payment to complete your order in Project Three!")
