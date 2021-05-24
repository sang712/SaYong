from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import History
from community.serializers import RatingSerializer, ReviewSerializer, CommentSerializer
from movies.serializers import MovieSerializer

class HistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = History
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    rating_set = RatingSerializer(many=True)
    review_set = ReviewSerializer(many=True)    # 작성한 리뷰
    comment_set = CommentSerializer(many=True)
    like_reviews = ReviewSerializer(many=True)  # 좋아요한 리뷰
    favorite_movies = MovieSerializer(many=True)    # 찜한 영화
    user_history = HistorySerializer(many=True)
    
    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = ('id', 'username', 'password', 'rating_set', 'review_set', 'like_reviews', 'comment_set', 'favorite_movies', 'user_history') # username만으로 접근이 안 되기 때문에 id값이 반드시 필요함
        # 필드에 추가하길 고려할만한 것: 이메일 주소, 지역, 계정과 이름의 구분 등
