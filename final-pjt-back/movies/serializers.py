# from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Genre, Movie
from community.serializers import RatingSerializer

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    rating_set = RatingSerializer(read_only=True, many=True)
    class Meta:
        model = Movie
        fields = '__all__'
