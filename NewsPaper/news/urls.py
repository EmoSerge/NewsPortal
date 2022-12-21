from django.urls import path
from .views import NewsList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete, ArticleCreate, CategoryListView, subscribe


urlpatterns = [
     path('', NewsList.as_view(), name='news'),
     path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
     path('create/', NewsCreate.as_view(), name='news_create'),
     path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
     path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
     path('article/create/', ArticleCreate.as_view(), name='article_create'),
     path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
     path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),

]
