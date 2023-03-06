from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class IndexPage(TemplateView):
    model = Article
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPage, self).get_context_data()
        articles = Article.objects.all().order_by('-created_at')[:12]
        context['articles'] = articles
        return context
