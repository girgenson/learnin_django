from django.shortcuts import render
from . models import News, Category


def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'Список новостей',
        }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    categories = Category.objects.all()
    news = News.objects.filter(category_id=category_id)
    context = {
        'news': news,
        'categories': categories,
    }
    return render(request, 'news/category.html', context)
