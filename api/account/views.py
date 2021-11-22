from logging import log
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from .forms import *
from .serializers import *
from rest_framework import status

        
@api_view(['POST']) 
def signup(request):
    serializer = UserSerializer(data=request.data) 
    if serializer.is_valid(raise_exception=True):
        serializer.save() # DB 저장

        return Response(serializer.data, status=201) 


from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        user = serializer.is_valid(raise_exception=True)
        if user:
            response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                # 'token' : serializer.data['token'],
                'message': 'User logged in  successfully',
                }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)



class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"Token": token.key})
        else:
            return Response(status=401)



def logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User Logged out successfully')
