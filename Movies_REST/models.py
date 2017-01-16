from django.db import models

# Create your models here.

GENRE = (
    (0, 'none'),
    (1, 'Sci-Fi'),
    (2, 'Horror'),
    (3, 'Comedy'),
    (4, 'Crime'),
    (5, 'Drama'),
    (6, 'Nonfiction'),
)

RANK = (
    (0, 'no ranking'),
    (1, 'rank 1'),
    (2, 'rank 2'),
    (3, 'rank 3'),
    (4, 'rank 4'),
    (5, 'rank 5'),
)
class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birth_date = models.DateField()
    birthplace = models.CharField(max_length=64)
    info = models.TextField(null=True)


    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Role(models.Model):
    role = models.CharField(max_length=128, primary_key=True)
    actor = models.ForeignKey('Person', on_delete=models.CASCADE, related_name="name")
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name="movie")

    def __str__(self):
        return self.role


class Movie(models.Model):

    title = models.CharField(max_length=128)
    director = models.ForeignKey('Person', related_name='movie_director')
    screenplay = models.ForeignKey('Person', related_name='movie_screenplay')
    starring = models.ManyToManyField('Person', through='Role')
    year = models.SmallIntegerField()
    ranking = models.SmallIntegerField(choices=RANK, default=0)
    genre = models.SmallIntegerField(choices=GENRE, default=0)

    class Meta:
        ordering = ['year']

    def __str__(self):
        return self.title

