from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Article, Category
from django.http import HttpResponseRedirect

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content', 'category', 'image']
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def like_article(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.user in article.likes.all():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def home(request):
    query = request.GET.get('q')
    articles = Article.objects.all()
    popular_articles = Article.objects.order_by('-total_likes')[:5]

    if query:
        articles = articles.filter(title__icontains=query)

    return render(request, 'blog/home.html', {'articles': articles, 'popular_articles': popular_articles})

def category_view(request, category):
    articles = Article.objects.filter(category=category)
    return render(request, 'blog/category.html', {'articles': articles, 'category': category})

