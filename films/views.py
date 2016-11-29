# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from films.models import Film
from films.serializers import FilmSerializer
import logging
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class FilmList(APIView):
    def get(self, request, format=None):
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
#        serializer = FilmSerializer(data=request.data)
        serializer = FilmWriteSerializer(data=request.data)
#        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilmDetail(APIView):
    """
    Retrieve, update or delete a film instance.
    """
    def get_object(self, pk):
        try:
            return Film.objects.get(pk=pk)
        except Film.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        film = self.get_object(pk)
        serializer = FilmSerializer(film)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        film = self.get_object(pk)
#        serializer = FilmSerializer(film, data=request.data)
        serializer = FilmWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        film = self.get_object(pk)
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class GenreList(APIView):
    """
    List all snippets, or create a new genre.
    """
    def get(self, request, format=None):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
    """
    Retrieve, update or delete a genre instance.
    """
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TheaterList(APIView):
    def get(self, request, format=None):
        theater = Theater.objects.all()
        serializer = TheaterSerializer(theater, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TheaterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TheaterDetail(APIView):
    """
    Retrieve, update or delete a theater instance.
    """
    def get_object(self, pk):
        try:
            return Theater.objects.get(pk=pk)
        except Theater.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        theater = self.get_object(pk=pk)
        serializer = TheaterSerializer(theater)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        theater = self.get_object(pk)
        serializer = TheaterSerializer(theater, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        theater = self.get_object(pk)
        theater.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
