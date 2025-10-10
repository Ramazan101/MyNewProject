from .models import Movie, Moments
from modeltranslation.translator import TranslationOptions,register

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('description','movie_name')


@register(Moments)
class MomentsTranslationOptions(TranslationOptions):
    fields = ('movie_moments',)

