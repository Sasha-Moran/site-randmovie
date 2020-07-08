from rest_framework import serializers
from rmovie.models import Movie

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'text', 'img', 'link', 'year', 'genre', 'movie_id']

class MovieRandApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'text', 'link', 'year', 'genre']
