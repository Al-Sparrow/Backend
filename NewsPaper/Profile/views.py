from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.shortcuts import render


class UserInfo(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts_info.html'
    context_object_name = 'accounts_info'

    def get_context_data(self, **kwargs):
        context_profile = super().get_context_data(**kwargs)
        context_profile['is_not_Author'] = not self.request.user.groups.filter(name='Author').exists()
        return context_profile


@login_required
def upgrade_me(request):
    user = request.user
    author_group = Group.objects.get(name='Author')
    if not user.groups.filter(name='Author').exists():
        author_group.user_set.add(user)
    return redirect('accounts_update')


class UserUpdate(LoginRequiredMixin, UpdateView):
    form_class = UserForm
    model = User
    template_name = 'accounts_update.html'
    success_url = reverse_lazy('accounts_info')


