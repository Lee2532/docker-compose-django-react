from django.contrib import admin
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # path('', views.signin, name='main'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('test/', views.ExampleView.as_view(), name='test'),
    
]