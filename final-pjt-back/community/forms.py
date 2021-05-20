from django import forms
from .models import Review, Comment, Rating


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'movie', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['review', 'user']


class RatingForm(forms.ModelForm):
    
    class Meta:
        model = Rating
        fields = ['rank']