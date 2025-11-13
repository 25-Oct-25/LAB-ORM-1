from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post

def index_view(request: HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by("-published_at")
    return render(request, "main/index.html", {"posts": posts})

def posts_view(request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        is_published = True if request.POST.get("is_published") == "on" else False

        Post.objects.create(
            title=title,
            content=content,
            is_published=is_published
        )

        return redirect("main:index_view")

    return render(request, "main/posts.html")
