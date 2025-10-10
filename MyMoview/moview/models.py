from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


STATUS_CHOICES = (('Diamond', 'Diamond'),
                  ('Gold', 'Gold'),
                  ('Bronze', 'Bronze'),
                  ('simple', 'Simple'),
                  )

class Profile(AbstractUser):
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(70)],
                              null=True, blank=True
                              )
    phone_number = PhoneNumberField()

    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='simple')


class Country(models.Model):
   country_name = models.CharField(max_length=50, unique=True)

   def __str__(self):
       return self.country_name

class Director(models.Model):
    director_name = models.CharField(max_length=50)
    bio = models.TextField(null=True, blank=True)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)],)
    director_image = models.ImageField(upload_to='director_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.director_name}, {self.bio}'


class Actor(models.Model):
    actor_name = models.CharField(max_length=50)
    bio = models.TextField()
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],)
    actor_image = models.ImageField(upload_to='actor_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.actor_name},{self.bio}'

class Genre(models.Model):
    Gere_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.Gere_name



class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    country = models.ManyToManyField(Country)
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)
    genre = models.ManyToManyField(Genre)
    TYPE_CHOICES = (
        ('144','144'),
        ('360','360'),
        ('480','480'),
        ('720', '1080'),)
    data_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    movie_time = models.PositiveSmallIntegerField()

    description = models.TextField()
    movie_trailer = models.FileField(upload_to='movie_trailers/')
    movie_image = models.ImageField(upload_to='movie_images/')
    status_movie = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return (f'{self.movie_name}, {self.year}, {self.director}, {self.actor}, {self.genre}, {self.movie_time},'
                f' {self.movie_trailer}, {self.movie_image}, {self.status_movie},{self.description},{self.country}')


class MovieLanguages(models.Model):
    movie_languages = models.CharField(max_length=32)
    video = models.FileField(upload_to='movie_video/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie}, {self.movie_languages}, {self.video}'

class Moments(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  movie_moments = models.ImageField(upload_to='movie_moments/')

class Rating(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.CharField(max_length=32, choices=[(i, str (i)) for i in range(1,11)])
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text}, {self.stars}, {self.movie}'


class Favorite(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.cart}, {self.movie}'

class History(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie}, {self.user}'


