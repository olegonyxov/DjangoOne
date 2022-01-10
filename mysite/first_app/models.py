from django.db import models
from django.utils.timezone import now


class Movie(models.Model):
    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3
    RATINGS = (
        (NOT_RATED, "NR - Not Rated"),
        (RATED_G, "G - General Audiences"),
        (RATED_PG, "PG - Parental Guidance" "Suggested"),
        (RATED_R, "R - Restricted")
    )
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField(default=2000)
    pub_date = models.DateField("date published", default=now())
    description = models.CharField(max_length=200, blank=True)
    url = models.URLField(max_length=200, blank=True)
    runtime = models.PositiveIntegerField(default=0)
    actor = models.ManyToManyField(
        to="Person",
        related_name="acting_credits",
        blank=True
    )
    director = models.ForeignKey(
        to="Person",
        null=True,
        on_delete=models.SET_NULL,
        related_name="directed",
        blank=True)
    rating = models.IntegerField(choices=RATINGS, default=NOT_RATED)

    class Meta:
        ordering = ("-year", "title")

    def __str__(self):
        return "{} ({})".format(self.title, self.year)


class Person(models.Model):
    name = models.CharField(max_length=50)
    born = models.DateField(blank=True)
    died = models.DateField(blank=True)
