from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from datetime import datetime
from django.urls import reverse_lazy
from .filters import PostFilter
from django.http import HttpResponse
from .forms import PostForm


def multiply(request):
   number = request.GET.get('number')
   multiplier = request.GET.get('multiplier')

   try:
       result = int(number) * int(multiplier)
       html = f"<html><body>{number}*{multiplier}={result}</body></html>"
   except (ValueError, TypeError):
       html = f"<html><body>Invalid input.</body></html>"
   return HttpResponse(html)


class PostList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'News.html'
    context_object_name = 'News'
    paginate_by = 5



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['filterset'] = self.filterset
        return context



class PostSearch(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'search.html'
    context_object_name = 'Search'
    paginate_by = 5

    def get_queryset(self):
         # Получаем обычный запрос
        queryset = super().get_queryset()
    #     # Используем наш класс фильтрации.
    #     # self.request.GET содержит объект QueryDict, который мы рассматривали
    #     # в этом юните ранее.
    #     # Сохраняем нашу фильтрацию в объекте класса,
    #     # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
    #     # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context



class PostDetail(DetailView):
    model = Post
    template_name = 'news_default.html'
    context_object_name = 'news_default'

    def get_context_data(self, **kwargs):
        context_detail = super().get_context_data(**kwargs)
        return context_detail



# Создание статьи
class PostCreate(CreateView):

    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

# Удаление статьи
class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
