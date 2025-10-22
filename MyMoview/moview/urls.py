from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import (ProfileViewSet, CountryListAPView,CountryDetailAPView,
                    ActorListAPView,ActorDetailAPIView, GenreListAPView,
                    GenreDetailAPIView, MovieListView, MovieDetailView,
                    RatingViewSet, FavoriteViewSet, FavoriteMovieViewSet, HistoryViewSet, RegisterView, CustomLoginView,
                    LogoutView, DirectorDetailAPIView, DirectorListAPIView)

from rest_framework import routers

router = DefaultRouter()
router.register('profile', ProfileViewSet)
router.register('rating', RatingViewSet)
router.register('favorite', FavoriteViewSet)
router.register('favorite-movie', FavoriteMovieViewSet)
router.register('history', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('movie/', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('director/', DirectorListAPIView.as_view(), name='director_detail'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('actor/', ActorListAPView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail'),
    path('genre/', GenreListAPView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),
    path('country/', CountryListAPView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPView.as_view(), name='country_detail'),
]