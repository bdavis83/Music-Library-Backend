from django.urls import path
from . import views

urlpattersns = [
    path('', views.songs_list),
  #  path ('<int:pk>/', views.songs_list),
]