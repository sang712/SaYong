from django.contrib.auth import get_user_model
from django.urls.conf import include
from rest_framework import serializers
from .models import History
from community.serializers import RatingSerializer, ReviewSerializer, CommentSerializer
from movies.serializers import MovieSerializer

class HistorySerializer(serializers.ModelSerializer):
# 여기엔 뭘 넣으면 .. 오류가 나네

    class Meta:
        model = History
        fields = '__all__'
        


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    rating_set = RatingSerializer(read_only=True, many=True)
    review_set = ReviewSerializer(read_only=True, many=True)    # 작성한 리뷰
    comment_set = CommentSerializer(read_only=True, many=True)
    like_reviews = ReviewSerializer(read_only=True, many=True)  # 좋아요한 리뷰
    favorite_movies = MovieSerializer(read_only=True, many=True)    # 찜한 영화
    user_history = HistorySerializer(read_only=True, many=True)
    # followings = serializers.IntegerField()

    class Meta:
        model = get_user_model()
        # fields = '__all__'
        # username만으로 접근이 안 되기 때문에 id값이 반드시 필요함
        # followers, followings 의 경우 Serializer에서 정의가 불가(자기참조 불가)하며, fields를 굳이하는 경우 models.py에 정의된 User에서 받아온다. 이 경우 많은 정보를 누락하거나, 불필요한 정보가 출력됨.
        fields = ('id', 'username', 'password', 'rating_set', 'review_set', 'like_reviews', 'comment_set', 'favorite_movies', 'user_history', 'followers', 'followings', 'is_superuser')
        # 필드에 추가하길 고려할만한 것: 이메일 주소, 지역, 계정과 이름의 구분 등
        # 무한루프에 빠지지 않게 깊이 1을 추가함
        depth = 1
