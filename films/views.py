from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from films.models import *
from films.serializers import *
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


@api_view(['GET', 'POST'])
def genre_list(request, format=None):
    """
    List all snippets, or create a new genre.
    """
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def genre_detail(request, pk, format=None):
    """
    Retrieve, update or delete a genre instance.
    """
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def film_list(request, format=None):
    """
    List all snippets, or create a new film.
    """
    if request.method == 'GET':
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #        serializedFilm = FilmWriteSerializer(data=request.data)
        serializer = FilmWriteSerializer(data=request.data)
#        print(serializer)
        if serializer.is_valid():
            serializer.save()
            #        return Response(serializedFilm.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def film_detail(request, pk, format=None):
    """
    Retrieve, update or delete a film instance.
    """
    try:
        film = Film.objects.get(pk=pk)
    except Film.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FilmSerializer(film)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def theater_list(request, format=None):
    """
    List all snippets, or create a new film.
    """
    if request.method == 'GET':
        theater = Theater.objects.all()
        serializer = TheaterSerializer(theater, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TheaterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def theater_detail(request, pk, format=None):
    """
    Retrieve, update or delete a film instance.
    """
    try:
        theater = Theater.objects.get(pk=pk)
    except Theater.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TheaterSerializer(theater)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TheaterSerializer(theater, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # films = serializer.films
        # print(films)
        # if films.is_valid():
        #     films.save()
        #     return Response(films.data)
        # return Response(films.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        theater.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def genre_films(request, pk, format=None):
    """
    Retrieve all films of a certain genre
    """
    try:
        films = Film.objects.all().filter(genre_id=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializedFilm = FilmSerializer(films, many=True)
        return Response(serializedFilm.data)


@api_view(['GET', 'PUT', 'DELETE'])
def theater_films(request, pk, format=None):
    """
    Retrieve all films at a given theater.
    """
    try:
        theater = Theater.objects.get(pk=pk)
    except Theater.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FilmSerializer(theater.film.all(), many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def film_theaters(request, pk, format=None):
    """
    Retrieve all theaters at which a given film is playing
    """
    try:
        film = Film.objects.get(pk=pk)
    except Film.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TheaterSerializer(film.theaters.all(), many=True)
        return Response(serializer.data)
