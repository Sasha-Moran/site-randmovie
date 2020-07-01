from django.shortcuts import render
from .models import Movie
from django.views.generic import View
from .forms import MovieForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.template.loader import render_to_string
import random

# from .utils import OdjectDetailMixin
# from .imdb import imdb_rating


def start_page(request):
    return render(request, 'rmovie/base.html')


def get_movie_ajax(request):
    if request.is_ajax():
        number_of_records = Movie.objects.all().count()
        rand_movie = random.randint(1, number_of_records)
        movie = Movie.objects.get(id=rand_movie)
        # movie_rating = imdb_rating(post.movie_id) , 'movie_rating': movie_rating
        rendered = render_to_string('rmovie/movie.html', context={'movie': movie})
        response = {'html': rendered}
        return JsonResponse(response)
    else:
        raise Http404


def about_project(request):
    count_of_movis_in_db = Movie.objects.all().count()
    return render(request, 'rmovie/about_project.html', context={'movies': count_of_movis_in_db})
