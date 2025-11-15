from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("posts/", views.posts_view, name="posts_view"),
]
