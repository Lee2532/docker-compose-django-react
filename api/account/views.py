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

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        user = serializer.is_valid(raise_exception=True)
        if user:
            logging.error(serializer)
            response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'token' :  serializer.data['token'],
                'message': 'User logged in  successfully',
                }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,) 

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

def logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User Logged out successfully')
