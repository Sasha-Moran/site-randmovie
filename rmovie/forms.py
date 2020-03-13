from django import forms
from .models import Movie

class MovieForm(forms.Form):
    title = forms.CharField(max_length=150)
    img = forms.CharField(max_length=600)
    text = forms.CharField(max_length=5000)
    link = forms.CharField(max_length=200)
    year = forms.CharField(max_length=6)
    genre = forms.CharField(max_length=50)
    movie_id = forms.CharField(max_length=50)

    title.widget.attrs.update({'class': 'form-control'})
    img.widget.attrs.update({'class': 'form-control'})
    text.widget.attrs.update({'class': 'form-control'})
    link.widget.attrs.update({'class': 'form-control'})
    year.widget.attrs.update({'class': 'form-control'})
    genre.widget.attrs.update({'class': 'form-control'})
    movie_id.widget.attrs.update({'class': 'form-control'})

    def save(self):
        new_movie = Movie.objects.create(title=self.cleaned_data['title'], img=self.cleaned_data['img'], body=self.cleaned_data['body'], link=self.cleaned_data['link'], year=self.cleaned_data['year'], genre=self.cleaned_data['genre'], movie_id=self.cleaned_data['movie_id'])
        return new_movie
