from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.

def home_view(request : HttpRequest):

    posts = Post.objects.all()

    return render(request, "main/home.html", {"posts" : posts})


def create_post_view(request : HttpRequest):

    if request.method == "POST":
        new_post = Post(title = request.POST["title"], 
                        content = request.POST["content"], 
                        is_published = request.POST.get("is_published") == "on", 
                        published_at = request.POST["published_at"])
        new_post.save()

    return render(request, "main/create.html")