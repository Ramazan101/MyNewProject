from django.contrib import admin
from .models import (Profile, Country, Director,
                     Actor, Genre, Movie, MovieLanguages, Moments, Rating, Favorite, FavoriteMovie, History)
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin

class MomentsInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Moments
    extra = 5

@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    inlines = [MomentsInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(MovieLanguages)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(FavoriteMovie)
admin.site.register(History)
admin.site.register(Genre)
