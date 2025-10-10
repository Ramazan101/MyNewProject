from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import (ProfileViewSet, CountryViewSet,DirectorViewSet,
                    ActorViewSet, GenreViewSet, MovieSetViewSet, MovieLanguagesViewSet,MomentsViewSet,
                    RatingViewSet, FavoriteViewSet, FavoriteMovieViewSet, HistoryViewSet, RegisterView, CustomLoginView, LogoutView)

from rest_framework import routers

router = DefaultRouter()
router.register('profile', ProfileViewSet)
router.register('country', CountryViewSet)
router.register('director', DirectorViewSet)
router.register('actor', ActorViewSet)
router.register('genre', GenreViewSet)
router.register('movie', MovieSetViewSet)
router.register('movie-languages', MovieLanguagesViewSet)
router.register('moments', MomentsViewSet)
router.register('rating', RatingViewSet)
router.register('favorite', FavoriteViewSet)
router.register('favorite-movie', FavoriteMovieViewSet)
router.register('history', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]