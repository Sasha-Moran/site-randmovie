from django.urls import path, include
from .views import *

urlpatterns = [
    path('', start_page, name='start_page'),
    path('get_movie/', get_movie,  name='get_movie' ),
    path('movies/', MoviesList.as_view(), name='list_movie_url'),
    path('add_movie/', MovieCreate.as_view(), name='create_movie_url'),
]
