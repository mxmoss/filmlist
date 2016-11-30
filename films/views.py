# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from films.models import Film, Genre, Theater
from films.serializers import FilmSerializer, GenreSerializer, TheaterSerializer
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

    def get(self, request, *args, **kwargs):
        begin_txt = request.GET.get('begins', '')
        year_prod = request.GET.get('year_prod', '0')
        # year_prod = 2012
#        pdb.set_trace()
        films = Film.objects.filter(year_prod__gte=year_prod, title__istartswith=begin_txt)
        if not films:
            return Response('there are no films that match the criteria')
        else:
            serialized_films = FilmSerializer(films, many=True)
            return Response(serialized_films.data)

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class TheaterList(generics.ListCreateAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

class TheaterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

