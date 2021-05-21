from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended', views.recommended, name='recommended'),
    # path('favorite/', views.favorite_index, name='favorite_index'),
    path('<int:movie_pk>/favorite/', views.favorite, name='favorite'),
]
