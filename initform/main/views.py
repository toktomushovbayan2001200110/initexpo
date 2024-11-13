from django.http import HttpResponse
from django.shortcuts import render


def index (request):
    data = {
       'title': 'Главная станица'
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
# views.py
from datetime import datetime

def home(request):
    contest_start_date = datetime(2025, 5, 1, 10, 0)  # Пример даты начала конкурса
    return render(request, 'index.html', {'contest_start_date': contest_start_date})
