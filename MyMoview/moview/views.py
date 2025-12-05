from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .filters import MovieFilter
from .models import (Profile, Country, Director, Actor, Genre, Movie,
                    MovieLanguages, Moments, Rating, Favorite, FavoriteMovie, History)

from .serializers import (ProfileSerializer,DirectorListSerializer,ActorListSerializer,
                        ActorDetailSerializer,
                        GenreListSerializers,GenreDetailSerializers, MovieListSerializer,MovieDetailSerializer,
                        MovieLanguagesSerializer, MomentsSerializer, RatingSerializer,CountryListSerializer, CountryDetailSerializer,
                        FavoriteMovieSerializer, FavoriteSerializer, HistorySerializer, UserSerializer, LoginSerializer,
                        DirectorDetailSerializer)
from rest_framework import viewsets, permissions, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .permissions import CheckStatus

from rest_framework.filters import SearchFilter, OrderingFilter

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CountryListAPView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer

class CountryDetailAPView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer


class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorListSerializer

class DirectorDetailAPIView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorDetailSerializer

class ActorListAPView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer

class ActorDetailAPIView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer

class GenreListAPView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializers

class GenreDetailAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreDetailSerializers

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['movie_name']
    ordering_fields = ['year']



class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    permission_classes = [CheckStatus]




class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteMovieViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMovieSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer











