from django.contrib import admin
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # path('', views.signin, name='main'),
    path('signup/', views.signup, name='signup'),
    path('test/', views.UserLoginView.as_view(), name='test'),
    path('test2/', views.LoginView.as_view(), name='test'),
    
]