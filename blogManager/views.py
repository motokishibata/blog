from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post, Category, SubCategory
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import PostForm
from django.urls import reverse, reverse_lazy

class PostListView(ListView):
    model = Post
    context_object_name = 'Posts'
    template_name = 'blogManager/index.html'

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'blogManager/create.html'

    def get_success_url(self):
        return reverse('blogManager:index')

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'Post'
    template_name = 'blogManager/detail.html'

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blogManager/update.html'

    def get_success_url(self):
        return reverse('blogManager:detail', kwargs={'pk': self.object.id})

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blogManager:index')
    template_name = 'blogManager/delete.html'
