from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'website/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'website/post_detail.html', {'post': post})
