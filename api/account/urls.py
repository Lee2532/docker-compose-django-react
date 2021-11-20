from django.contrib import admin
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # path('', views.signin, name='main'),
    path('', views.Signup.as_view(), name='signup'),
]