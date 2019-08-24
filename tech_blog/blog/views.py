from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView,CreateView, DeleteView, UpdateView)
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.utils import timezone

class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    models = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    models = Post

class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    success_url =reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).orderby('-create_date')
