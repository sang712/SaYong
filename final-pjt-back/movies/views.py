from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Movie, Genre
from accounts.views import logHistory
# from community.forms import RatingForm
from rest_framework import serializers, status
from rest_framework.response import Response
from .serializers import *
from accounts.serializers import *
from rest_framework.decorators import  api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
@api_view(['GET'])
def index(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    sorted_serializer = sorted(serializer.data, key=lambda k: k['popularity'], reverse=True)
    return Response(sorted_serializer)

@api_view(['GET'])
def genre(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def recommended(request):
    recommended_movie = get_list_or_404(Movie)
    serializer = MovieSerializer(recommended_movie)
    return Response(serializer.data)

# def favorite_index(request):
#     pass
    # M:N관계에서는 어떤 serializer를 사용해야하는가?
    # accounts의 followers 를 참조하자
    # favorite_relations = get_list_or_404()


# if request.user.is_authenticated:
@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def favorite(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        users = movie.favorite_users.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        user = request.user
        if movie.favorite_users.filter(pk=user.pk).exists():
            movie.favorite_users.remove(user)
            logHistory(user, 21, movie=movie)
            # preLog = History.objects.get(user=user, following=person)
            # preLog.is_public = False
        else:
            movie.favorite_users.add(user)
            logHistory(user, 20, movie=movie)
        users = movie.favorite_users.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)