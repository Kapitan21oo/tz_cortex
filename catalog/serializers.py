from rest_framework import serializers
from .models import Artist, Album, Song, AlbumSong


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Song
        fields = '__all__'


class AlbumSongSerializer(serializers.ModelSerializer):
    song = SongSerializer()

    class Meta:
        model = AlbumSong
        fields = '__all__'