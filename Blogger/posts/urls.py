from django.urls import path
from . import views


app_name = "posts"

urlpatterns = [
  path("add-post/", views.add_post_view, name="add_post_view"),
  path("create-post/", views.create_post, name="create_pos" ),
]