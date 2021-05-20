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
                logHistory(user, 1, person.pk, 11)
            else:
                person.followers.add(user)
                logHistory(user, 1, person.pk, 10)
    return redirect('accounts:profile', person.username)

def logHistory(user, object_type, object_pk, action_type):
    '''
    object type - action_type
    1: 계정 -팔로우: 10 /언팔로우: 11
    2: 영화 -찜하기: 20 /찜 해제: 21
    3: 별점 -남겼: 30 /취소: 31
    4: 리뷰 -남겼: 30 /취소: 31 /좋아요: 50 /좋아요 취소: 51
    5: 댓글 -남겼: 30 /취소: 31
    '''
    form = HistoryForm()
    history = form.save(commit=False)
    
    history.user = user
    history.object_type = object_type
    history.object_pk = object_pk
    history.action_type = action_type
    
    if action_type%10:
        history.is_public = False
        
    history.save()