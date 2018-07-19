# Create your models here.
from django.db import models


class Artist(models.Model):
    artist_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)