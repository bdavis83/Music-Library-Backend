from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongsSerializer
from .models import Songs
from django.shortcuts import get_object_or_404

