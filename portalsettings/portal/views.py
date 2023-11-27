from django.shortcuts import render
from .models import News

# Create your views here.

def home(request):
    # news = [
    #     {
    #         'title': 'Наша первая статья',
    #         'text': 'Полный текст статьи',
    #         'date': '22.08.1997',
    #         'author': 'Вельмакин Н. А.'
    #     },
    #     {
    #         'title': 'Наша вторая статья',
    #         'text': 'Полный текст статьи',
    #         'date': '01.05.2001',
    #         'author': 'Лукина Н. А.'
    #     }
    # ]

    data = {
        'news': News.objects.all(),
        'title': 'Главная страница'
    }
    return render(request, 'portal/home.html', data)

def about(request):
    return render(request, 'portal/about.html')

def contacts(request):
    return render(request, 'portal/contacts.html')