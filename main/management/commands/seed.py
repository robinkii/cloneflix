from django.core.management.base import BaseCommand
from faker import Faker
import random
from main.models import CustomUser, Profile, Genre, Show, Episode, Movie, Review, SubscriptionType, Subscription, ViewingHistory, Watchlist

class Command(BaseCommand):
    help = 'Seed database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create genres
        genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Sci-Fi', 'Thriller']
        for genre in genres:
            Genre.objects.create(label=genre)

        # Create users and profiles
        for _ in range(10):
            user = CustomUser.objects.create(
                email=fake.email(),
                username=fake.user_name(),
                password_hash=fake.password()
            )
            Profile.objects.create(
                user=user,
                profile_name=fake.name(),
                profile_picture=fake.image_url()
            )

        # Create shows
        for _ in range(10):
            show = Show.objects.create(
                title=fake.catch_phrase(),
                description=fake.text(),
                release_date=fake.date(),
                average_rating=random.uniform(1, 10),
                picture=fake.image_url()
            )
            # Assign random genres to show
            for genre in Genre.objects.order_by('?')[:random.randint(1, 3)]:
                show.genres.add(genre)

        # Create episodes
        for show in Show.objects.all():
            for season in range(1, random.randint(2, 5)):
                for episode_number in range(1, random.randint(10, 20)):
                    Episode.objects.create(
                        show=show,
                        season=season,
                        episode_number=episode_number,
                        title=fake.catch_phrase(),
                        description=fake.text(),
                        duration=random.randint(20, 60),
                        release_date=fake.date()
                    )

        # Create movies
        for _ in range(10):
            movie = Movie.objects.create(
                title=fake.catch_phrase(),
                description=fake.text(),
                picture=fake.image_url(),
                release_date=fake.date(),
                average_rating=random.uniform(1, 10),
                duration=random.randint(60, 180)
            )
            # Assign random genres to movie
            for genre in Genre.objects.order_by('?')[:random.randint(1, 3)]:
                movie.genres.add(genre)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
