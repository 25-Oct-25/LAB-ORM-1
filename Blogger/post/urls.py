from django.urls import path
from . import views


app_name = "post"

urlpatterns=[
   path('',views.home_view,name="home_view"),
   path('add-post/',views.add_post_view,name="add_post_view"),
]