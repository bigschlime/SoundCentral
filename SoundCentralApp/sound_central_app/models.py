from django.db import models


# Create your models here.

class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    spotify_artist_uri = models.URLField()  # Store Spotify URI for direct linking
    apple_music_artist_uri = models.URLField()  # Store Apple Music URI for direct linking
    youtube_music_artist_uri = models.URLField()  # Store Youtube Music URI for direct linking

    def str(self):
        return f"{self.name}  (ID: {self.artist_id})"


class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    total_tracks = models.IntegerField()
    spotify_album_uri = models.URLField()  # Store Spotify URI for direct linking
    apple_music_album_uri = models.URLField()  # Store Apple Music URI for direct linking
    youtube_music_album_uri = models.URLField()  # Store Youtube Music URI for direct linking


def str(self):
    return f"{self.name} - {self.artist_id} (ID: {self.album_id})"


class Track(models.Model):
    track_id = models.AutoField(primary_key=True)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artists = models.ManyToManyField(Artist)
    name = models.CharField(max_length=255)
    duration_ms = models.IntegerField()
    explicit = models.BooleanField()
    spotify_track_uri = models.URLField()  # Store Spotify URI for direct linking
    apple_music_track_uri = models.URLField()  # Store Apple Music URI for direct linking
    youtube_music_track_uri = models.URLField()  # Store Youtube Music URI for direct linking
    track_number = models.IntegerField()


def str(self):
    return f"{self.name} - {self.artist} (ID: {self.track_id})"
