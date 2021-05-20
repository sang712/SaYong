from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Review, Comment
from .forms import ReviewForm, CommentForm, RatingForm
from accounts.views import logHistory
from movies.models import Movie

@require_GET
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST) 
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            logHistory(review.user, 30, review=review)
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_GET
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        logHistory(comment.user, 30, comment=comment)
        return redirect('community:detail', review.pk)
    context = {
        'comment_form': comment_form,
        'review': review,
        'comments': review.comment_set.all(),
    }
    return render(request, 'community/detail.html', context)


@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            logHistory(request.user, 51, review=review)
        else:
            review.like_users.add(user)
            logHistory(request.user, 50, review=review)
        return redirect('community:index')
    return redirect('accounts:login')


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