from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from rest_framework.serializers import Serializer
from .models import Review, Comment
# from .forms import ReviewForm, CommentForm, RatingForm
from accounts.views import logHistory
from movies.models import Movie
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@api_view(['GET'])
def review_index(request):
    reviews = Review.objects.order_by('-pk')
    serializer = ReviewSerializer(reviews, many=True)
    # 잠시 확인을 위해 추가하였음
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)
    # 여기까지
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def review_create(request, movie_pk):
    serializer = ReviewSerializer(data=request.data)
    movie = get_object_or_404(Movie, pk=movie_pk)
    if serializer.is_valid(raise_exception=True):
        review = serializer.save(movie=movie)
        logHistory(request.user, 30, review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        # 댓글들을 어떻게 리뷰를 호출할 때 같이 가져올 것인가. 어디선가 배웠는데?
        # comments = review.comment_set.all()
        # comment_form = CommentForm()
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
def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
        # review_detail GET 요청과 동일함. 굳이 GET이 필요한가에 대한 의문 발생
    elif request.method == 'POST':
        user = request.user
        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            logHistory(request.user, 51, review=review)
        else:
            review.like_users.add(user)
            logHistory(request.user, 50, review=review)
        # Response가 따로 필요 없다? like에 대한 반응은 vue.js에서 처리


@api_view(['GET'])
def rating_index(request):
    ratings = Rating.objects.all()
    serializer = RatingSerializer(ratings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def rating_create(request, movie_pk):
    serializer = RatingSerializer(data=request.data)
    movie = get_object_or_404(Movie, pk=movie_pk)
    if serializer.is_valid(raise_exception=True):
        review = serializer.save(user=request.user, movie=movie)
        logHistory(request.user, 30, review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def rating_detail(request, rating_pk):
    rating = get_object_or_404(Rating, pk=rating_pk)
    if request.method == 'GET':
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            logHistory(request.user, 32, rating=rating)
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        logHistory(request.user, 31, rating=rating)
        rating.delete()
        data = {
            'delete':f'{rating_pk}번 평점이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def comment_index(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        comment = serializer.save(review=review, user=request.user)
        logHistory(request.user, 30, comment=comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return render(request, 'movies/detial.html', context)

@api_view(['GET','PUT','DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
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
        logHistory(request.user, 31, comment=comment)
        comment.delete()
        data = {
            'delete':f'{comment_pk}번 평점이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
