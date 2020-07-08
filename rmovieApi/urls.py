from django.urls import path
from .views import *


urlpatterns = [
    path('randmovie/', RandMovie.as_view()),
    path('movie/list/', APIMovieList.as_view(), name="apimovielist"),
    path('movie/add/', APIMovieAdd.as_view()),
]
