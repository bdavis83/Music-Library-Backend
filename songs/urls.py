from django.urls import path
from . import views

urlpattersns = [
    path ('<int:pk>/', views.songs_list),
]