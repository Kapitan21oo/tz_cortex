from django.db import models
from rest_framework import viewsets


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title + ' / ' + str(self.artist)


class Song(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    track_number = models.PositiveIntegerField()
    def __str__(self):
        return 'Album: '+str(self.album) + ' / Song: ' + str(self.song) + ' / Track number: ' + str(self.track_number)

    class Meta:
        unique_together = ['track_number']

