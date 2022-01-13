from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
    path('movies/', views.movies_all, name='movies_all'),
    path('movies/top/', views.movies_top_ten, name='movies_top_ten'),
    path('movies/top/<int:top_input>/', views.movies_top_input, name='movies_top_input'),
    path('movies/<str:input_title>/', views.movies_info, name='movies_info'),
    path('movies/rate+/<str:input_title>/', views.movie_rate_up, name='movies_rate_up'),
    path('movies/rate-/<str:input_title>/', views.movie_rate_down, name='movies_rate_down'),


]
