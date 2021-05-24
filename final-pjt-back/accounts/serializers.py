from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import History


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = ('id', 'username', 'password') # username만으로 접근이 안 되기 때문에 id값이 반드시 필요함
        # 필드에 추가하길 고려할만한 것: 이메일 주소, 지역, 계정과 이름의 구분 등


class HistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = History
        fields = '__all__'