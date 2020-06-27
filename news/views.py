from django.shortcuts import render, get_object_or_404, redirect
from . models import News, Category
from . forms import NewsForm


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


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)  # Форма, связанная с данными
        # Пользователю не нужно будет ее повторно заполнять при неверном заполнении
        if form.is_valid():
            # print(form.cleaned_data)
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()  # Форма, не связанная с данными
    return render(request, 'news/add_news.html', {'form': form})
