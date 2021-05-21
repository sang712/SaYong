from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .models import History
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HistorySerializer, UserSerializer

def index(request):
    pass

def modify(request):
    pass


# if request.user.is_authenticated:
#     return redirect('community:index')
@api_view(['POST'])
def signup(request):
    # Client에서 온 데이터를 받기
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	# 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	# UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	# validation 작업 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save() # 유저 인스턴스 만들기
        # 비밀번호 해싱 
        user.set_password(request.data.get('password')) # 장고에 내장되어있는 함수
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 로그인과 로그아웃은 지우기
# if request.user.is_authenticated:
#     return redirect('community:index')
@require_http_methods(['GET', 'POST'])
def login(request):
    print(request.user)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:review_index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    print(request.user)
    auth_logout(request)
    return redirect('community:index')


# if request.user.is_authenticated:
#     return redirect('community:index')
# history가 프로필이 아니라 다른 페이지에서 보이도록 수정해야함
@api_view(['GET', 'PUT', 'DELETE'])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    # logHistory = History.objects.all()
    # context = {
    #     'person': person,
    #     'logHistory': logHistory,
    # }
    serializer = UserSerializer(person)
    return Response(serializer.data, status=status.HTTP_200_OK)


# if request.user.is_authenticated:
@require_POST
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    user = request.user
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
            logHistory(user, 11, following=person)
        else:
            person.followers.add(user)
            logHistory(user, 10, following=person)
        return Response(status=status.HTTP_200_OK)
    # return redirect('accounts:profile', person.username)

@api_view(['GET'])
def history(request):
    histories = get_list_or_404(History)
    serializer = HistorySerializer(histories)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


def logHistory(user, action_type, **kwargs):
    '''
    object - action_type
    계정 -팔로우: 10 /언팔로우: 11 /회원가입: 110
    영화 -찜하기: 20 /찜 해제: 21 /영화추가: 210 /영화삭제: 211 /영화수정:212
    별점 -남겼: 30 /취소: 31
    리뷰 -남겼: 30 /취소: 31 /수정: 32 /좋아요: 50 /좋아요 취소: 51
    댓글 -남겼: 30 /취소: 31
    '''
    
    data = {}
    for key, value in kwargs.items():
        if key == 'following':
            data['following'] = value.pk
        elif key == 'movie':
            data['movie'] = value.pk
        elif key == 'rating':
            data['rating'] = value.pk
        elif key == 'review':
            data['review'] = value.pk
        elif key == 'comment':
            data['comment'] = value.pk
    
    data['user'] = user.pk
    data['action_type'] = action_type
    print(data)
    
    if action_type%10:
        data['is_public'] = False
        
    history = HistorySerializer(data=data)
    if history.is_valid(raise_exception=True):
        history.save()