from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users (superheroes)
        marvel_heroes = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com'},
            {'name': 'Captain America', 'email': 'cap@marvel.com'},
            {'name': 'Black Widow', 'email': 'widow@marvel.com'},
        ]
        dc_heroes = [
            {'name': 'Superman', 'email': 'superman@dc.com'},
            {'name': 'Batman', 'email': 'batman@dc.com'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com'},
        ]
        users = []
        for hero in marvel_heroes:
            users.append(User.objects.create(name=hero['name'], email=hero['email'], team=marvel))
        for hero in dc_heroes:
            users.append(User.objects.create(name=hero['name'], email=hero['email'], team=dc))

        # Create workouts
        workout1 = Workout.objects.create(name='Push Ups', description='Upper body workout', difficulty='Easy')
        workout2 = Workout.objects.create(name='Running', description='Cardio workout', difficulty='Medium')
        workout3 = Workout.objects.create(name='Deadlift', description='Strength workout', difficulty='Hard')

        # Create activities
        for user in users:
            Activity.objects.create(user=user, workout=workout1, duration_minutes=20, calories_burned=100)
            Activity.objects.create(user=user, workout=workout2, duration_minutes=30, calories_burned=250)
            Activity.objects.create(user=user, workout=workout3, duration_minutes=15, calories_burned=200)

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=1000)
        Leaderboard.objects.create(team=dc, total_points=900)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
