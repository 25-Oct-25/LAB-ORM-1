from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('heritage/', views.heritage_view, name='heritage_view'),
    path('add/', views.add_post, name='add_post'),
]
