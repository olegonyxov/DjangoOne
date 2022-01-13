import random

from django.core.management.base import BaseCommand
from faker import Faker
from first_app.models import Movie


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--len", type=int, default=2)

    def handle(self, *args, **options):
        faker = Faker()
        self.stdout.write("Start inserting Movies")
        for i in range(options['len']):
            self.stdout.write("Start inserting Movies")
            movie = Movie()
            new_title = " ".join(faker.text().split()[:3])
            movie.title = "Forsage - " + new_title
            movie.description = faker.text()
            movie.year = random.randint(1990, 2022)
            movie.user_rating = random.randint(0, 100)
            movie.save()
            self.stdout.write(f"New Movie: {movie}")
        self.stdout.write("End inserting Movies")

