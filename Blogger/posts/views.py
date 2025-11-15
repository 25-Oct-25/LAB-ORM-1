from django.shortcuts import render , redirect
from .models import Post
from django.utils import timezone



# Create your views here.

def home_view(request):

    posts=Post.objects.all()

    return render(request,'posts/home.html',{'posts':posts})

def add_post_view(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published=request.POST.get('is_published') == 'on'
        published_at=request.POST.get('published_at')
        if not published_at:
            published_at = timezone.now()

        Post.objects.create(title=title, content=content, is_published=is_published,published_at=published_at)
        return redirect('posts:home_view')

    return render(request,'posts/add_post.html')
