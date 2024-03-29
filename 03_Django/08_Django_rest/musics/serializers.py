from rest_framework import serializers
from .models import Music, Artist, Comment

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist', )
        

class ArtistSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer()

    class Meta:
        model = Artist
        fields = ('id', 'name',)

class ArtistDetailSerializer(ArtistSerializer):
    musics = MusicSerializer(source="music_set", many=True)
    musics_count = serializers.IntegerField(source='music_set.count')

    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ('musics', 'musics_count',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id', )

class MusicDetailSeiralizer(MusicSerializer):
    comments = CommentSerializer(source='comment_set', many=True)
    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ('comments', )