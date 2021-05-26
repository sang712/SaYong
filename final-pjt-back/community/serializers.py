from rest_framework import serializers
from .models import Review, Comment, Rating



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'  # content, review, user
        # exclude = ['review', 'user']


class ReviewSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(read_only=True, many=True)
    
    class Meta:
        model = Review
        fields = '__all__'  # title, content, movie, user, like_users
        # fields = ['title', 'content']


class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rating
        fields = '__all__'  # rank, movie, user
        # fields = ['rank']