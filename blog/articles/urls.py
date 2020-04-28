from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

urlpatterns = [
    path('articles/', ArticleListView.as_view(),
         name='articles'),
    path('articles/article/<int:pk>/', ArticleDetailView.as_view(),
         name='article'),
    path('articles/create/', ArticleCreateView.as_view(),
         name='create_article'),
    path('articles/article/<int:pk>/update/', ArticleUpdateView.as_view(),
         name='update_article'),
    path('articles/article/<int:pk>/delete', ArticleDeleteView.as_view(),
         name='delete_article')
]
