from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

# User model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CustomUserManager()

    def __str__(self):
        return self.username

# Profile model
class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile_name

# Genre model
class Genre(models.Model):
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label

# Show model
class Show(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    average_rating = models.FloatField()
    date_added = models.DateField(auto_now_add=True)
    picture = models.ImageField(upload_to='show_pictures', blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='shows')

    def __str__(self):
        return self.title

# Episode model
class Episode(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    season = models.IntegerField()
    episode_number = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # Duration in minutes
    release_date = models.DateField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.show.title} S{self.season}E{self.episode_number} - {self.title}"

# Movie model
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='movie_pictures', blank=True, null=True)
    release_date = models.DateField()
    average_rating = models.FloatField()
    duration = models.IntegerField()  # Duration in minutes
    date_added = models.DateField(auto_now_add=True)
    genres = models.ManyToManyField(Genre, related_name='movies')

    def __str__(self):
        return self.title

# Review model
class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, null=True, blank=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.FloatField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.movie:
            return f"Review of {self.movie.title} by {self.user.username}"
        elif self.show:
            return f"Review of {self.show.title} by {self.user.username}"
        elif self.episode:
            return f"Review of {self.episode.title} by {self.user.username}"
        else:
            return f"Review by {self.user.username}"

# SubscriptionType model
class SubscriptionType(models.Model):
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label

# Subscription model
class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.FloatField()
    type = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s subscription"

# ViewingHistory model
class ViewingHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, null=True, blank=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, null=True, blank=True)
    watched_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s viewing history"

# Watchlist model
class Watchlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, null=True, blank=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s watchlist"
