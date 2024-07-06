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
                username=fake.user_name()
            )
            user.set_password(fake.password())  # Hash the password
            user.save()

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

        # Create subscription types
        subscription_types = ['Basic', 'Standard', 'Premium']
        for st in subscription_types:
            SubscriptionType.objects.create(label=st)

        # Create subscriptions
        for user in CustomUser.objects.all():
            Subscription.objects.create(
                user=user,
                start_date=fake.date_this_year(),
                end_date=fake.date_this_year(),
                cost=random.uniform(10.0, 100.0),
                type=SubscriptionType.objects.order_by('?').first()
            )

        # Create reviews
        for user in CustomUser.objects.all():
            for _ in range(5):
                Review.objects.create(
                    user=user,
                    movie=Movie.objects.order_by('?').first() if random.choice([True, False]) else None,
                    show=Show.objects.order_by('?').first() if random.choice([True, False]) else None,
                    episode=Episode.objects.order_by('?').first() if random.choice([True, False]) else None,
                    rating=random.uniform(1.0, 10.0),
                    review_text=fake.text(),
                    created_at=fake.date_time_this_year()
                )

        # Create viewing histories
        for user in CustomUser.objects.all():
            for _ in range(10):
                ViewingHistory.objects.create(
                    user=user,
                    movie=Movie.objects.order_by('?').first() if random.choice([True, False]) else None,
                    show=Show.objects.order_by('?').first() if random.choice([True, False]) else None,
                    episode=Episode.objects.order_by('?').first() if random.choice([True, False]) else None,
                    watched_on=fake.date_this_year()
                )

        # Create watchlists
        for user in CustomUser.objects.all():
            profile = Profile.objects.filter(user=user).first()
            for _ in range(10):
                Watchlist.objects.create(
                    user=user,
                    profile=profile,
                    movie=Movie.objects.order_by('?').first() if random.choice([True, False]) else None,
                    show=Show.objects.order_by('?').first() if random.choice([True, False]) else None,
                    episode=Episode.objects.order_by('?').first() if random.choice([True, False]) else None,
                    date_added=fake.date_this_year()
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
