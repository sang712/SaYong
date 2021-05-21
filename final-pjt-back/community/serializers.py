from rest_framework import serializers
from .models import Review, Comment, Rating


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'  # title, content, movie, user, like_users
        # fields = ['title', 'content']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'  # content, review, user
        # exclude = ['review', 'user']


class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rating
        fields = '__all__'  # rank, movie, user
        # fields = ['rank']