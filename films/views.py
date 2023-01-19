# from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from films.models import Film, Genre, Theater
from films.serializers import * #FilmSerializer, FilmWriteSerializer, GenreSerializer, TheaterSerializer, UserSerializer
import logging
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
import pdb
from django.urls import re_path
from rest_framework_swagger.views import get_swagger_view
from rest_framework.pagination import PageNumberPagination
from films.permissions import IsOwnerOrReadOnly
import requests

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

schema_view = get_swagger_view(title='Pastebin API')

@api_view(['GET'])
def film_title(request, format=None):
    #get a list of films
    if request.method == 'GET':
#        films = requests.get('http://www.omdbapi.com/?type=movie&s=hunger')
        payload = request.query_params #GET.keys()
        if not(payload):
            payload = {'type': 'movie', 's': 'any'}
        films = requests.get('http://www.omdbapi.com/', params=payload)
        json = films.json()
        a = []
        for key in json['Search']:
            films_dict = {}
            films_dict['title'] = key['Title']
            films_dict['year_prod'] = key['Year']
            a.append(films_dict)
        serializedFilm = FilmSerializer(a, many=True)
#        if serializedFilm.is_valid():
#            serializedFilm.save()
        return Response(serializedFilm.data)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 100
#
class ShortResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10

class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    pagination_class =  ShortResultsSetPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if(self.request.method == 'GET'):
            return FilmSerializer
        return FilmWriteSerializer

    def get(self, request, *args, **kwargs):
# #this commented-out line shows how to get an arbitrary param
#        self.request.GET.get('user')
        k = request.GET.keys()
        filter_dict = {}
        if(k):
            for key, value in request.GET.items():
                filter_dict[key] = value
            films = Film.objects.filter(**filter_dict)
            serialized_films = FilmSerializer(films, many=True)
            return Response(serialized_films.data)
        else:
            serialized_films = FilmSerializer(Film.objects.all(), many=True)
            return Response(serialized_films.data)


class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if (self.request.method == 'GET'):
            return GenreSerializer
        return GenreWriteSerializer

    def get(self, request, *args, **kwargs):
        k = request.GET.keys()
        filter_dict = {}
        if(k):
            for key, value in request.GET.items():
                filter_dict[key] = value
            genres = Genre.objects.filter(**filter_dict)
            serialized_genres = GenreSerializer(genres, many=True)
            return Response(serialized_genres.data)
        else:
            serialized_genres = GenreSerializer(Genre.objects.all(), many=True)
            return Response(serialized_genres.data)

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        if (self.request.method == 'GET'):
            return GenreSerializer
        return GenreWriteSerializer

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class TheaterList(generics.ListCreateAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TheaterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer


