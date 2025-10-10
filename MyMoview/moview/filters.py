from .models import Movie
from django_filters import filterset

class MovieFilter(filterset.FilterSet):
    class Meta:
        model = Movie
        fields = {
            'country' : ['exact'],
            'director' : ['exact'],
            'actor' : ['exact'],
            'year' : ['gt','lt'],
            'genre' : ['exact'],
            'status_movie' : ['exact'],
        }