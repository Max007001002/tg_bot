from django.shortcuts import render
from django.db.models import Count
from .models import Request  # Импортируем модель Request для использования в статистике

def home(request):
    return render(request, 'home.html')

def start(request):
    return render(request, 'start.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def stats(request):
    # Получаем статистику по часам
    hourly_stats = Request.objects.values('timestamp__hour').annotate(num_requests=Count('id'))

    return render(request, 'stats.html', {'hourly_stats': hourly_stats})
