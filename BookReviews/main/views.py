from django.shortcuts import render, redirect
from .models import Post   


def home_view(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, "main/index.html", {"posts": posts})
 

def add_post_view(request):

    
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            content=request.POST["content"]
        )
        return redirect("main:home_view")

    return render(request, "main/add.html")
