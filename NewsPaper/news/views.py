from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
from pprint import pprint

class PostList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'News.html'
    context_object_name = 'News'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_time_news'] = "Новости еженедельно, по пятницам!"
        pprint(context)
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news_default.html'
    context_object_name = 'news_default'

    def get_context_data(self, **kwargs):
        context_detail = super().get_context_data(**kwargs)
        return context_detail



