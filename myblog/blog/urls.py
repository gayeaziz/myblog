from django.urls import path
from .views import ArticleListView, ArticleDetailView, like_article
from blog import views

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog-home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:pk>/like/', like_article, name='like-article'),
    path('categorie/<str:category>/', views.category_view, name='category-view'),

    
]
