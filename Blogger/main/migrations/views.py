from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def index_view(request):
    font_size = request.COOKIES.get('font_size', 'normal')  
 
    return render(request, "main/index.html", {'font_size': font_size})


def heritage_view(request):
    return render(request, "main/heritage.html")


def home(request):
    posts = Post.objects.filter(is_published=True).order_by("-published_at")  
    return render(request, "main/index.html", {"posts": posts})

def add_post(request):
    if request.method == "POST": 
        form = PostForm(request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('home')  
        else:
   
            return render(request, "main/add_post.html", {"form": form, "error": "تأكد من البيانات المدخلة"})
    else:
        form = PostForm()  

    return render(request, "main/add_post.html", {"form": form})  
