from django.db import models
from django.utils.timezone import now


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField(default=2000)
    pub_date = models.DateField("date published", default=now())
    description = models.CharField(max_length=200, blank=True)
    url = models.URLField(max_length=200, blank=True)
    runtime = models.PositiveIntegerField(default=0)
    user_rating = models.PositiveIntegerField(default=5)

    class Meta:
        ordering = ("-year", "title")

    def __str__(self):
        return "{} ({}) ({})".format(self.title, self.year, self.user_rating)

