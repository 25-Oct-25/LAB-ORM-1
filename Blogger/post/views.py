from django.shortcuts import render ,redirect
from django.http import HttpRequest
from django.utils import timezone
from .models import Post

# Create your views here.

def home_view(request:HttpRequest):
    posts=Post.objects.all().order_by('-published_at')
    return render(request,"post/home.html", {"posts":posts})


def add_post_view(request:HttpRequest):
    if request.method =="POST":
        is_published = request.POST.get("is_published")=="True"
        new_post = Post(title=request.POST["title"],content=request.POST["content"],is_published=is_published, published_at=timezone.now())
        new_post.save()
        return redirect("post:home_view")
    return render(request,"post/create.html")