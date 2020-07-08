from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import random


from .serializers import MovieSerializer, MovieRandApiSerializer
from rmovie.models import Movie


class APIMovieList(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class APIMovieAdd(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class RandMovie(APIView):
    def get(self, request):
        movieset = Movie.objects.all()
        randmovie = random.choice(movieset)
        serializer = MovieRandApiSerializer(randmovie)
        return Response(serializer.data)
