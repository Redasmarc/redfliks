from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.movie, name='movie'),
    path('nitflex_movie_list/', views.MovieGroupNListView.as_view(), name='nitflex_movie_list'),
    path('hpo_movie_list/', views.MovieGroupHListView.as_view(), name='hpo_movie_list'),
    path('disnep_movie_list/', views.MovieGroupDListView.as_view(), name='disnep_movie_list'),
]