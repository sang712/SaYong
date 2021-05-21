from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('review/', views.review_index, name='review_index'),
    path('<int:movie_pk>/review/', views.review_create, name='review_create'),
    path('review/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('review/<int:review_pk>/like/', views.review_like, name='review_like'),
    path('rating/', views.rating_index, name='rating_index'),
    path('<int:movie_pk>/rating/', views.rating_create, name='rating_create'),
    path('rating/<int:rating_pk>/', views.rating_detail, name='rating_detail'),
    path('comment/', views.comment_index, name='comment_index'),
    path('<int:review_pk>/comment/', views.comment_create, name='comment_create'),
    path('comment/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
]
