from django.shortcuts import render, HttpResponse

# Create your views here.

def blog_home(request):
    return HttpResponse("Welcome to the Blog Home of Project Four!")

def latest_posts(request):
    return HttpResponse("Check out the latest blog posts here.")

def blog_post_detail(request):
    return HttpResponse("Here is the detailed view of a selected blog post.")

def post_comment(request):
    return HttpResponse("Share your thoughts by commenting on this post!")

def author_profile(request):
    return HttpResponse("Learn more about the author on this page.")
