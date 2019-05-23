from django.shortcuts import render
from blog.models import Post

def index(request):
    Posts = Post.objects.order_by('update_time')
    context = {'Posts': Posts}
    return render(request, 'blogManager/index.html', context)

def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'Post': post}
    return render(request, 'blogManager/edit.html', context)
