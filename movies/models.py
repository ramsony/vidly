from django.db import models
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.FloatField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
