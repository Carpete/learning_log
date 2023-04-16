"""Defines URL patterns for users"""

from django.urls import path, include

from . import views 

app_name = 'users'
urlpatterns = [
    #Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    #Registration page
    path('register/', views.register, name='register'),
]

"""Correct login redirect error"""
#LOGIN_REDIRECT_URL = 'learning_logs:index'

#LOGIN_URL = 'login'