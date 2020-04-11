from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Назва')
    text = models.TextField(verbose_name='Пост')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата створення')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публыкації')

    class Meta:
        verbose_name_plural = 'Пости'
        verbose_name = 'Пост'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
