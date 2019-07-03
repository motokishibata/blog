from django.shortcuts import render
from .models import Post

def index(request):
    Posts = Post.objects.filter(active=True).order_by('update_time')
    context = {'Posts': Posts}
    return render(request, 'blog/index.html', context)

def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'Post': post}
    return render(request, 'blog/detail.html', context)

def manage(request):
    return render(request, 'admin/index.html')