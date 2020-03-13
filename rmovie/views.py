from django.shortcuts import render
from .models import Movie
from django.views.generic import View
from .forms import MovieForm
from django.contrib.auth.mixins import LoginRequiredMixin
# from .utils import OdjectDetailMixin
import random
# from .imdb import imdb_rating


def start_page(request):
    return render(request, 'rmovie/base_main.html')


def get_movie(request):
    number_of_records = Movie.objects.all().count()
    rand_movie = random.randint(1, number_of_records)
    post = Movie.objects.get(id=rand_movie)
    # movie_rating = imdb_rating(post.movie_id) , 'movie_rating': movie_rating
    return render(request, 'rmovie/extended_page.html', context={'post': post})


def about_project(request):
    count_of_movis_in_db = Movie.objects.all().count()
    return render(request, 'rmovie/about_project.html', context={'movies': count_of_movis_in_db})


class MoviesList(LoginRequiredMixin, View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'rmovie/page_movies.html', context={'movies': movies})


class  MovieCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = MovieForm()
        return render(request, 'rmovie/create_movie.html', context={'form':form})
        raise_exception = True

    def post(self, request):
        bound_form = MovieForm(request.POST)

        if bound_form.is_valid():
            new_movie = bound_form.save()
            return render(request, 'rmovie/create_info.html')
        return render(request, 'rmovie/create_movie.html', context={'form': bound_form })
