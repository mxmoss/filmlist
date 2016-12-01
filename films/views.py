# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from films.models import Film, Genre, Theater
from films.serializers import * #FilmSerializer, FilmWriteSerializer, GenreSerializer, TheaterSerializer
import logging
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
import pdb

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

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

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_serializer_class(self):
        if (self.request.method == 'GET'):
            return GenreSerializer
        return GenreWriteSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class TheaterList(generics.ListCreateAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

class TheaterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

