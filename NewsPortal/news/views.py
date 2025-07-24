
from django.shortcuts import render, get_object_or_404
from .models import Post

def news_list(request):
    posts = Post.objects.filter(post_type=Post.NEWS).order_by('-created_at')
    return render(request, 'news/news_list.html', {'posts': posts})

def news_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news/news_detail.html', {'post': post})