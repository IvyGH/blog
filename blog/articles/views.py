from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Article
from .forms import ArticleModelForm


class ArticleListView(ListView):
    """ Article list view """
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    """ Article detail view """
    model = Article
    template_name = 'articles/articles_detail.html'
    context_object_name = 'article'


class ArticleCreateView(CreateView):
    """ Article create view """
    form_class = ArticleModelForm
    model = Article
    template_name = 'articles/articles_create.html'
    success_url = '/'


class ArticleUpdateView(UpdateView):
    """ Article update view """
    form_class = ArticleModelForm
    model = Article
    template_name = 'articles/articles_update.html'
    success_url = '/'


class ArticleDeleteView(DeleteView):
    """ Article delete view """
    model = Article
    template_name = 'articles/articles_delete.html'
    success_url = '/'
