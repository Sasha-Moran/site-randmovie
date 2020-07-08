from django.urls import path, include
from .views import *

urlpatterns = [
    path('', start_page, name='start_page'),
    path('get_movie_ajax/', get_movie_ajax, name='get_movie_ajax'),
    path('about_project/', about_project, name='about_project' ),
]
