from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Назва фільму')
    text = models.TextField(db_index=True, verbose_name='Опис')
    img = models.CharField(max_length=600, verbose_name='Постер до фільму')
    link = models.CharField(max_length=200, verbose_name='Силка на трейлер')
    year = models.CharField(max_length=6, verbose_name='Рік виходу')
    genre = models.CharField(max_length=50, verbose_name='Жанр')
    movie_id = models.CharField(max_length=50, verbose_name='ID IMDB')

    class Meta:
        verbose_name_plural = 'Фільми'
        verbose_name = 'Фільм'

    def __str__(self):
        return self.title
