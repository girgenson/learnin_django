from django.shortcuts import render
from . models import News, Category


def index(request):
    news = News.objects.order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'category': categories
        }
    return render(request, 'news/index.html', context)
