from rest_framework import serializers
from films.models import Genre, Film, Theater

class FilmSerializer(serializers.ModelSerializer):
    theater_set = serializers.StringRelatedField(many=True, required=False, )
#    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), required=False,)
    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre', 'theater_set')
        depth = 1

class GenreSerializer(serializers.ModelSerializer):
    film_set = FilmSerializer(many=True, required=False,)
    class Meta:
        model = Genre
        fields = ('id', 'description', 'film_set')

class TheaterSerializer(serializers.ModelSerializer):
    films = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all(), allow_null=True, required=False,)
    class Meta:
        model = Theater
        fields = ('id', 'name', 'city', 'state', 'num_screens', 'digital', 'comment_txt', 'films')

class FilmWriteSerializer(serializers.ModelSerializer):
    theater_set = serializers.StringRelatedField(many=True, required=False, )
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), allow_null=True)

    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre', 'theater_set')

class GenreWriteSerializer(serializers.ModelSerializer):
    film_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all(), allow_null=True, required=False,)
    class Meta:
        model = Genre
        fields = ('id', 'description', 'film_set')

