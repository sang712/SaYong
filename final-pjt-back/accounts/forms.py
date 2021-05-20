from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import History


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class HistoryForm(forms.ModelForm):
    
    class Meta:
        model = History
        fields = '__all__'