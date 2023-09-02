from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


@property
def movies_count(self):
    return self.movie_set.all().count()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


@property
def reviews(self):
    return self.movie_reviews.filter(stars__gt=3)


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    stars = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

