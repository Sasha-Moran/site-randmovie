from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    search_fields = ('title', 'text', 'year', 'genre')

admin.site.register(Movie, MovieAdmin)
