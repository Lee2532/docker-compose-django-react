import logging
from .models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def create(self, validated_data):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match'})

        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import update_last_login

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        user = authenticate(username=username, password=password)
        logging.error(user)
        if user is None:
            raise serializers.ValidationError(
                'ID 또는 PW가 틀렸습니다.'
            )

        token = Token.objects.get_or_create(user=user)[0].key
        
        return {
            'username': user.username,
            'token': token
        }