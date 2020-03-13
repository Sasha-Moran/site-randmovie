from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    text = models.TextField(db_index=True)
    img = models.CharField(max_length=600)
    link = models.CharField(max_length=200)
    year = models.CharField(max_length=6)
    genre = models.CharField(max_length=50)
    movie_id = models.CharField(max_length=50)

    def __str__(self):
        return self.title
