from django.contrib.auth import get_user_model
from django.urls.conf import include
from rest_framework import serializers
from .models import History


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # followings = serializers.IntegerField()
    
    class Meta:
        model = get_user_model()
        # fields = include('username', 'password')
        exclude = ('last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions')
        # 필드에 추가하길 고려할만한 것: 이메일 주소, 지역, 계정과 이름의 구분 등
        # 무한루프에 빠지지 않게 깊이 1을 추가함
        depth = 1
   
        
class HistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = History
        fields = '__all__'