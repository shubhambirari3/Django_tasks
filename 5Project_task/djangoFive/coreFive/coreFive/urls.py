"""
URL configuration for coreFive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homeFive import views

urlpatterns = [
    path('blog/', views.blog_home),
    path('blog/posts/',views.latest_posts),
    path('blog/posts/detail/', views.blog_post_detail),
    path('blog/posts/comment/', views.post_comment),
    path('blog/author/', views.author_profile),
]
