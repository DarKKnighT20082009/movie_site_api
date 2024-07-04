from django.db import models
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    release_year = models.IntegerField()
    description = models.TextField()
    rating = models.FloatField()

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
