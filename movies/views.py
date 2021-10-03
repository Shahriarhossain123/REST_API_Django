from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializers
from .models import MoviesData


# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.all()
    serializer_class = MovieSerializers


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(typ='action')
    serializer_class = MovieSerializers


class HorrorViewSet(viewsets.ModelViewSet):
    queryset = MoviesData.objects.filter(typ='horror')
    serializer_class = MovieSerializers
