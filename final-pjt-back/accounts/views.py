from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm, HistoryForm
from .models import History


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('community:index')


@login_required
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    logHistory = History.objects.all()
    context = {
        'person': person,
        'logHistory': logHistory,
        
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                logHistory(user, 11, following=person)
                # preLog = History.objects.get(user=user, following=person)
                # preLog.is_public = False
            else:
                person.followers.add(user)
                logHistory(user, 10, following=person)
    return redirect('accounts:profile', person.username)

def logHistory(user, action_type, **kwargs):
    '''
    object - action_type
    계정 -팔로우: 10 /언팔로우: 11 /회원가입: 110
    영화 -찜하기: 20 /찜 해제: 21
    별점 -남겼: 30 /취소: 31
    리뷰 -남겼: 30 /취소: 31 /좋아요: 50 /좋아요 취소: 51
    댓글 -남겼: 30 /취소: 31
    '''
    form = HistoryForm()
    history = form.save(commit=False)
    
    for key, value in kwargs.items():
        if key == 'following':
            history.following = value
        elif key == 'movie':
            history.movie = value
        elif key == 'rating':
            history.rating = value
        elif key == 'review':
            history.review = value
        elif key == 'comment':
            history.comment = value
    
    history.user = user
    
    history.action_type = action_type
    
    if action_type%10:
        history.is_public = False
        
    history.save()