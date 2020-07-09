from django.shortcuts import render, get_object_or_404, redirect
from . models import News, Category
from . forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'}
    queryset = News.objects.select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    model = News
    # Используем тот же самый шаблон потому что вывод ничем не отличается:
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id']).select_related('category')


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'
    #template_name = 'news/news_detail.html'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')


# def index(request):
#     news = News.objects.order_by('-created_at')
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#         }
#     return render(request, 'news/index.html', context)


# def get_category(request, category_id):
#     categories = Category.objects.all()
#     news = News.objects.filter(category_id=category_id)
#     context = {
#         'news': news,
#         'categories': categories,
#     }
#     return render(request, 'news/category.html', context)
#
#
# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {"news_item": news_item})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)  # Форма, связанная с данными
#         # Пользователю не нужно будет ее повторно заполнять при неверном заполнении
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()  # Форма, не связанная с данными
#     return render(request, 'news/add_news.html', {'form': form})
