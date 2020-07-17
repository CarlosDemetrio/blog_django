from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'website/index.html', {'posts': posts})