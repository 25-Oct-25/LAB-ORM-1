from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.utils.translation import gettext_lazy as _
from .models import Post

# Create your views here.

def add_post_view(request:HttpRequest):
  return render(request, "posts/add-post.html")

def create_post(request:HttpRequest):

  title = request.POST.get("title")
  content = request.POST.get("content")

  post = Post.objects.create(title=title,content=content) 

  messages.success(request, _("Post Created Successfully"))

  return redirect(request.META.get("HTTP_REFERER", "/"))