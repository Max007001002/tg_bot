from django.urls import path
from . import views

urlpatterns = [
    path("", views.start, name="start"),
    path('home/', views.home, name='home'),  # Исправлен путь для главной страницы
    path("chatbot/", views.chatbot, name='chatbot'),
    path('stats/', views.stats, name='stats'),  # Новый путь для страницы статистики
]
