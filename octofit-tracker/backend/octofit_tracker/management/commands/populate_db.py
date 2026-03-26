from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        db = connection.cursor().db_conn.client[settings.DATABASES['default']['NAME']]
        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Teams
        marvel_team = {'name': 'Team Marvel', 'members': ['Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow', 'Spider-Man']}
        dc_team = {'name': 'Team DC', 'members': ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Cyborg']}
        marvel_team_id = db.teams.insert_one(marvel_team).inserted_id
        dc_team_id = db.teams.insert_one(dc_team).inserted_id

        # Users
        users = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': marvel_team_id},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team': marvel_team_id},
            {'name': 'Thor', 'email': 'thor@marvel.com', 'team': marvel_team_id},
            {'name': 'Hulk', 'email': 'hulk@marvel.com', 'team': marvel_team_id},
            {'name': 'Black Widow', 'email': 'widow@marvel.com', 'team': marvel_team_id},
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': marvel_team_id},
            {'name': 'Superman', 'email': 'superman@dc.com', 'team': dc_team_id},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': dc_team_id},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': dc_team_id},
            {'name': 'Flash', 'email': 'flash@dc.com', 'team': dc_team_id},
            {'name': 'Aquaman', 'email': 'aquaman@dc.com', 'team': dc_team_id},
            {'name': 'Cyborg', 'email': 'cyborg@dc.com', 'team': dc_team_id},
        ]
        db.users.insert_many(users)

        # Activities
        activities = [
            {'user': 'Iron Man', 'activity': 'Running', 'duration': 30},
            {'user': 'Batman', 'activity': 'Cycling', 'duration': 45},
            {'user': 'Wonder Woman', 'activity': 'Swimming', 'duration': 60},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'team': 'Team Marvel', 'points': 120},
            {'team': 'Team DC', 'points': 110},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {'name': 'Morning Cardio', 'description': 'Cardio workout for all'},
            {'name': 'Strength Training', 'description': 'Strength workout for heroes'},
        ]
        db.workouts.insert_many(workouts)

        # Create unique index on email
        db.users.create_index([('email', 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
