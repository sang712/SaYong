from rest_framework import serializers
from .models import Review, Comment, Rating


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ['title', 'movie', 'content']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = ['review', 'user']


class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rating
        fields = ['rank']