from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, User, Author
from django.urls import reverse_lazy, reverse
from .filters import PostFilter
from django.http import HttpResponse
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from django.views.generic import TemplateView


def multiply(request):
   number = request.GET.get('number')
   multiplier = request.GET.get('multiplier')

   try:
       result = int(number) * int(multiplier)
       html = f"<html><body>{number}*{multiplier}={result}</body></html>"
   except (ValueError, TypeError):
       html = f"<html><body>Invalid input.</body></html>"
   return HttpResponse(html)





class PostList(LoginRequiredMixin, ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'News.html'
    context_object_name = 'News'
    paginate_by = 5



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['filterset'] = self.filterset
        return context


class PostSearch(LoginRequiredMixin, ListView):
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


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'news_default.html'
    context_object_name = 'news_default'

    def get_context_data(self, **kwargs):
        context_detail = super().get_context_data(**kwargs)
        return context_detail


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, Form):
        # authorUser = self.request.user.objects.get(id=int(self.kwargs['pk']))
        Form.instance.author = Author.objects.get(authorUser = self.request.user)
        return super().form_valid(Form)



class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    raise_exception = True
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class CommentPost (LoginRequiredMixin, CreateView):
    form_class = CommentForm
    model = Comment
    template_name = 'comment.html'


    def form_valid(self, Form):
        Form.instance.commentPost_id = Post.objects.get(id=int(self.kwargs['pk'])).id
        Form.instance.commentUser_id = self.request.user.id
        return super().form_valid(Form)



