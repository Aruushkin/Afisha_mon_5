from django.db import models
from movie_app.choices import CHOICES


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    @property
    def movies_count(self):
        return self.movie_set.all().count()


class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.DateTimeField()

    def __str__(self):
        return str(self.director)

    @property
    def reviews(self):
        return self.movie_reviews.filter(stars__gt=3)


class Review(models.Model):
    text = models.TextField(
        null=True,
        blank=True
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        null=True,
        related_name='movie_reviews'
    )
    stars = models.IntegerField(
        default=5,
        choices=CHOICES
    )

    def __str__(self):
        return str(self.movie)
