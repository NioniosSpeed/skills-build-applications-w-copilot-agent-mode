from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class ModelTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration_minutes=10, calories_burned=50)
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100)

    def test_user(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.team, self.team)

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_activity(self):
        self.assertEqual(self.activity.user, self.user)
        self.assertEqual(self.activity.workout, self.workout)

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.team, self.team)
        self.assertEqual(self.leaderboard.total_points, 100)
