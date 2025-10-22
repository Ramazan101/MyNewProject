from .models import Movie, Moments, Country, Director, Actor, MovieLanguages, Genre
from modeltranslation.translator import TranslationOptions,register

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('description','movie_name')

@register(Moments)
class MomentsTranslationOptions(TranslationOptions):
    fields = ('movie_moments',)

@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('actor_name',)

@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('director_name',)

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(MovieLanguages)
class MovieLanguagesTranslationOptions(TranslationOptions):
    fields = ('movie_languages',)

@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('Gere_name',)
