
from .models import (Profile, Country, Director, Actor, Genre, Movie,
                    MovieLanguages, Moments, Rating, Favorite, FavoriteMovie, History)
from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','country_name']

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','country_name']



class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id','director_name']

class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id','director_name']





class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id','actor_name']


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id','actor_name']



class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','Gere_name']

class GenreListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','Gere_name']


class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%Y')
    country = CountrySerializer(many=True)
    genre = GenreSerializers(many=True)


    class Meta:
        model = Movie
        fields = ['id', 'movie_name','year','country','genre','status_movie']

class DirectorDetailSerializer(serializers.ModelSerializer):
    director_movie = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Director
        fields = ['bio','director_name','director_image','age','director_movie']


class ActorDetailSerializer(serializers.ModelSerializer):
    actor_movie = MovieListSerializer(many=True, read_only=True)


    class Meta:
        model = Actor
        fields = ['actor_image','actor_name','age','bio','actor_movie']


class GenreDetailSerializers(serializers.ModelSerializer):
    genre_movie = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ['Gere_name']


class CountryDetailSerializer(serializers.ModelSerializer):
    country_name = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['country_name']

class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['id','movie_languages','video']

class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']


class MovieDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format=('%d-%m-%Y'))
    country = CountrySerializer(many=True)
    director = DirectorSerializer(many=True)
    actor = ActorSerializer(many=True)
    genre = GenreSerializers(many=True)
    videos = MovieLanguagesSerializer(many=True, read_only=True)
    moments = MomentsSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()


    class Meta:
        model = Movie
        fields = ['movie_name','year','country','genre',
                  'director','actor','data_type','description',
                  'movie_time','movie_trailer','movie_image','status_movie','videos','moments',
                  'ratings','get_avg_rating','get_count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()




class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'



