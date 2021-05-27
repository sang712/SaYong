from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Review, Comment
# from .forms import ReviewForm, CommentForm, RatingForm
from accounts.views import logHistory
from movies.models import Movie
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_index(request):
    reviews = Review.objects.order_by('-pk')
    serializer = ReviewSerializer(reviews, many=True)
    # # 잠시 확인을 위해 추가하였음
    # context = {
    #     'reviews': reviews,
    # }
    # return render(request, 'community/index.html', context)
    # # 여기까지
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    serializer = ReviewSerializer(data=request.data)
    movie = get_object_or_404(Movie, pk=movie_pk)
    if serializer.is_valid(raise_exception=True):
        review = serializer.save(movie=movie)
        logHistory(request.user, 30, review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        # 댓글들을 어떻게 리뷰를 호출할 때 같이 가져올 것인가. 어디선가 배웠는데?
        # comments = review.comment_set.all()
        # comment_form = CommentForm()
        # 해결법: serializers.py에서 변수로 해당 serializer 삽입
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logHistory(request.user, 32, review=review)
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        logHistory(request.user, 31, review=review)
        review.delete()
        data = {
            'delete':f'{review_pk}번 리뷰가 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

# if request.user.is_authenticated:
#     return redirect('accounts:login')
@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        pass # if-elif 분기 이후로 이동
        # review_detail GET 요청과 동일함. 굳이 GET이 필요한가에 대한 의문 발생
    elif request.method == 'POST':
        user = request.user
        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            logHistory(request.user, 51, review=review)
        else:
            review.like_users.add(user)
            logHistory(request.user, 50, review=review)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def rating_index(request):
    ratings = Rating.objects.all()
    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def rating_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        rating = serializer.save(user=request.user, movie=movie)
        if rating.rank: # 별을 다시 클릭하는 경우를 평점 취소로 받아 들여서 rank를 0을 보내줌
            logHistory(request.user, 30, rating=rating, movie=movie)
        else: # 0을 보내줄 때는 action_type을 31로
            logHistory(request.user, 31, rating=rating, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def rating_detail(request, rating_pk):
    rating = get_object_or_404(Rating, pk=rating_pk)
    movie = get_object_or_404(Movie, pk=rating.movie)
    if request.method == 'GET':
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logHistory(request.user, 32, rating=rating, movie=movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        logHistory(request.user, 31, rating=rating, movie=movie)
        rating.delete()
        data = {
            'delete':f'{rating_pk}번 평점이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def comment_index(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = get_object_or_404(get_user_model(), pk=request.data['user'])
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        comment = serializer.save(review=review, user=user)
        logHistory(user, 30, comment=comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET','PUT','DELETE'])
def comment_detail(request, comment_pk):
    print('데이터', request.data, request.user)
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = get_object_or_404(get_user_model(), pk=request.data['user'])
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logHistory(request.user, 32, comment=comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        logHistory(user, 31, comment=comment)
        comment.delete()
        data = {
            'delete':f'{comment_pk}번 평점이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
