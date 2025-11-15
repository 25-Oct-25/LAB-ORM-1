from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from posts.models import Post

# Create your views here.
def home_view(request:HttpResponse):

    return render(request, 'main/home.html')