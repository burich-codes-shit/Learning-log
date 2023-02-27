""" Определяет схемы URL для пользователей """
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    #Включить url авторизации по-умолчанию
    path('', include('django.contrib.auth.urls')),
    #Страниа регистрации
    path('register/', views.register, name='register'),
]