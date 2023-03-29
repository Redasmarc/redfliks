from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views import generic
from . import models
from user_profile.models import Profile

# Create your views here.

@login_required
def index(request):
    profile = get_object_or_404(Profile, user=request.user)
    if not profile.choice_1 and profile.choice_2 and profile.choice_3:
        return render(request, 'flexzone/choose.html')
    movie_count = models.Movie.objects.count()
    return render(request, 'flexzone/index.html', {
        'movie_count': movie_count,
    })



# @login_required
# def movies(request):
#     profile = get_object_or_404(Profile, user=request.user)
#     if not profile.choice_1:
#         # User doesn't have a subscription pack of 'n'
#         return redirect('flexzone/no_access.html')
    
#     movies = models.Movie.objects.all()
#     context = {
#         'movies': movies,
#     }
#     return render(request, 'flexzone/movies.html', context)

@login_required
def movie(request, movie_id):
    movie = get_object_or_404(models.Movie, id=movie_id)
    profile = get_object_or_404(Profile, user=request.user)
    if not profile.choice_1:
        return render(request, 'flexzone/no_access.html')
    return render(request, 'flexzone/movie.html', {
    'movie': movie,
    'choice': profile,})

class MovieGroupNListView(generic.ListView):
    template_name = 'flexzone/nitflex_movie_list.html'
    context_object_name = 'nitflex_movie_list'
    paginate_by = 3

    def get_queryset(self):
        return models.Movie.objects.filter(group='n')

class MovieGroupHListView(generic.ListView):
    template_name = 'flexzone/hpo_movie_list.html'
    context_object_name = 'hpo_movie_list'
    paginate_by = 3

    def get_queryset(self):
        return models.Movie.objects.filter(group='h')

class MovieGroupDListView(generic.ListView):
    template_name = 'flexzone/disnep_movie_list.html'
    context_object_name = 'disnep_movie_list'
    paginate_by = 3

    def get_queryset(self):
        return models.Movie.objects.filter(group='d')