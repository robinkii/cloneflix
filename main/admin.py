from django.contrib import admin
from .models import CustomUser, Profile, Genre, Show, Episode, Movie, Review, SubscriptionType, Subscription, ViewingHistory, Watchlist

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Genre)
admin.site.register(Show)
admin.site.register(Episode)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(SubscriptionType)
admin.site.register(Subscription)
admin.site.register(ViewingHistory)
admin.site.register(Watchlist)




