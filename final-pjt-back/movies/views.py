from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Movie
from accounts.views import logHistory
from community.forms import RatingForm


# Create your views here.
@require_GET
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = RatingForm()
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/detail.html', context)


@require_GET
def recommended(request):
    pass

@require_POST
def favorite(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user

        if movie.favorite_users.filter(pk=user.pk).exists():
            movie.favorite_users.remove(user)
            logHistory(user, 21, movie=movie)
            # preLog = History.objects.get(user=user, following=person)
            # preLog.is_public = False
        else:
            movie.favorite_users.add(user)
            logHistory(user, 20, movie=movie)
        return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')