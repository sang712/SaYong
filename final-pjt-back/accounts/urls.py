from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('follow/<int:user_pk>/', views.follow, name='follow'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('history/', views.history, name='history'),
    # JWT 토큰

    path('<int:user_pk>/history/', views.user_history, name='user_history'),
    path('<int:user_pk>/favorite/', views.user_favorite, name='user_favorite'),
    path('<int:user_pk>/following/', views.following, name='following'),
    path('<int:username>/', views.profile, name='profile'),
    # 반드시 맨 하단에 있어야함
    path('<str:username>/', views.profile, name='profile'),
]
