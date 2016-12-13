from rest_framework import routers, pagination, serializers
from films.models import Genre, Film, Theater
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    films = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all())
    theaters = serializers.PrimaryKeyRelatedField(many=True, queryset=Theater.objects.all(), required=False, )
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all(), allow_null=True)

    class Meta:
        model = User
        fields= ('id','username', 'films', 'theaters', 'genres')

class FilmSerializer(serializers.ModelSerializer):
    theater_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Theater.objects.all(), required=False, )
    owner = serializers.ReadOnlyField(source='owner.username')
#    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), required=False,)
    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre', 'theater_set', 'owner')
        depth = 1

class GenreSerializer(serializers.ModelSerializer):
    film_set = FilmSerializer(many=True, required=False,)
    class Meta:
        model = Genre
        fields = ('id', 'description', 'film_set')

class TheaterSerializer(serializers.ModelSerializer):
    films = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all(), allow_null=True, required=False,)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Theater
        fields = ('id', 'name', 'city', 'state', 'num_screens', 'digital', 'comment_txt', 'films', 'owner')

class FilmWriteSerializer(serializers.ModelSerializer):
    theater_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Theater.objects.all(), required=False, )
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), allow_null=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre', 'theater_set', 'owner')

class GenreWriteSerializer(serializers.ModelSerializer):
    film_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all(), allow_null=True, required=False,)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Genre
        fields = ('id', 'description', 'film_set', 'owner')

