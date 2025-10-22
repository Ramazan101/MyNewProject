from .models import Movie
from django_filters import filterset

class MovieFilter(filterset.FilterSet):
    class Meta:
        model = Movie
        fields =  {
            'country': ['exact'],
            'year': ['gt', 'lt'],
            'director': ['exact'],
            'actor': ['exact'],
            'genre': ['exact'],
            'status_movie': ['exact'],

        }