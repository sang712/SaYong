from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from rest_framework.serializers import Serializer
from .models import Review, Comment
from .forms import ReviewForm, CommentForm, RatingForm
from accounts.views import logHistory
from movies.models import Movie
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@api_view(['GET'])
def index(request):
    reviews = Review.objects.order_by('-pk')
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            review = serializer.save()
            logHistory(request.user, 30, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# @require_GET
@api_view(['GET'])
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # 댓글들을 어떻게 리뷰를 호출할 때 같이 가져올 것인가. 어디선가 배웠는데?
    # comments = review.comment_set.all()
    # comment_form = CommentForm()
    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=request.user)
        logHistory(request.user, 30, comment=comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# if request.user.is_authenticated:
#     return redirect('accounts:login')
@api_view(['GET','POST'])
def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        user = request.user
        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            logHistory(request.user, 51, review=review)
        else:
            review.like_users.add(user)
            logHistory(request.user, 50, review=review)
        # return redirect('community:index')
        # Response가 따로 필요 없다? like에 대한 반응은 vue.js에서 처리


@require_POST
def rating(request, movie_pk):
    if request.method == 'POST':
        form = RatingForm(request.POST) 
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.users
            rating.movie_id = movie_pk
            rating.save()
            logHistory(rating.user, 30, rating=rating)
            return redirect('movies:detail', movie_pk)
    else:
        form = RatingForm()
    context = {
        'form': form,
        'movie_pk': movie_pk,
    }
    return render(request, 'movies/detial.html', context)