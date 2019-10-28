from django.shortcuts import render,get_object_or_404
from .models import Artist, Music, Comment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSeiralizer


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    
    # serialiezer: Queryset -> json 으로 변환
    serializer = MusicSerializer(musics,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicDetailSeiralizer(music)
    return Response(serializer.data)

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request,artist_pk):
    artist = get_object_or_404(Artist,pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

@api_view(['POST'])
def comments_create(request, music_pk):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def comments_update_and_delete(request,comment_pk):
    # PUT
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method =='PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Comment has been updated!!'})
    # DELETE
    else:
        comment.delete()
        return Response({'message': ' Comment has been deleted!'})