from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongsSerializer
from .models import Songs
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def songs_list (request):
    
    if request.method == 'GET':
        songs_var = Songs.objects.all()
        song_serializer = SongsSerializer (songs_var, many=True)
        custom_response_dict = {
            'song': song_serializer.data
        }
        return Response (custom_response_dict)

    elif request.method == 'POST':
        serializer = SongsSerializer (data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data, status = status.HTTP_201_CREATED)
