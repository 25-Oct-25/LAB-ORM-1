from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.

def home_view(request:HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by('-published')
    return render(request, 'main/home.html', {"posts":posts})

def add_post_view(request:HttpRequest):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        is_published = request.POST.get("is_published") == "on"

        new_post = Post(
            title=title,
            content=content,
            is_published=is_published
        )
        new_post.save() 
        return redirect("main:home")
    return render(request,'main/add_post.html')