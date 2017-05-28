from django.db import models
import datetime
from datetime import date

# Create your models here.

class Album(models.Model):
    album_name = models.CharField(max_length=250)
    album_artist = models.CharField(max_length=250)
    album_count= models.IntegerField(default=1)
    album_logo = models.CharField(max_length=1000)
    album_genre = models.CharField(max_length=250)

    def __str__(self):
        return self.album_name + '-'+ self.album_artist

class Songs(models.Model):
    #Assuming an album has various artists and songs are of various genre
    song_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    song_artist = models.CharField(max_length=250)
    song_genre = models.CharField(max_length=250)
    song_length = models.DecimalField(decimal_places=2,max_digits=5)
    song_type = models.CharField(max_length=10)

    def __str__(self):
        return self.song_title