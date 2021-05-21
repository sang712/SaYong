from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import History


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = ('username', 'password')
        # 필드에 추가하길 고려할만한 것: 이메일 주소, 지역, 계정과 이름의 구분 등


class HistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = History
        fields = '__all__'