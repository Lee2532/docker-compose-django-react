from logging import log
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from .forms import *
from .serializers import *

        
@api_view(['POST']) 
@permission_classes([AllowAny])
def signup(request):
    serializer = UserSerializer(data=request.data) 
    if serializer.is_valid(raise_exception=True):
        serializer.save() # DB 저장
        return Response(serializer.data, status=201) 


from django.contrib.auth import authenticate

@api_view(['GET']) 
@permission_classes([AllowAny])
def test(request):
    user = authenticate(username='test8', password='0000')
    if user is None:
        data = {'status' : 'user is None'}
    else:
        data = {'status' : 'user is Not None'}
    return JsonResponse(data)