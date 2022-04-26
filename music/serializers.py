from rest_framework import serializers
from .models import Song

#here I am importing the use of the Song app to serialize its data
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title", "artist", "album", "release", "genre", "likes"]

