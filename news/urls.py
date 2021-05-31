import debug_toolbar

from django.urls import path, include
from .views import *


urlpatterns = [
    # path('', index, name='home'),
    path('news/', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>', get_category, name='category'),
    path('news/category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('<int:news_id>', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('add_news', add_news, name='add_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),

    path('contact/', contact, name='contact'),
    path('', HomeNews.as_view(), name='home'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
