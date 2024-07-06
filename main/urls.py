from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet, GenreViewSet, ShowViewSet, EpisodeViewSet, MovieViewSet, ReviewViewSet, SubscriptionTypeViewSet, SubscriptionViewSet, ViewingHistoryViewSet, WatchlistViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'shows', ShowViewSet)
router.register(r'episodes', EpisodeViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'subscriptiontypes', SubscriptionTypeViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'viewinghistories', ViewingHistoryViewSet)
router.register(r'watchlists', WatchlistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]