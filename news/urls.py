from django.urls import path
from .views import *


urlpatterns = [
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('<int:news_id>', view_news, name='view_news'),
    path('<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('add_news', add_news, name='add_news'),
    path('add_news/', CreateNews.as_view(), name='add_news'),
]
