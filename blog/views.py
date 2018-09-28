from django.shortcuts import render
from django.utils import timezone
from .models import Post

def base(request):
    posts = Post.objects.filter(data_publi__lte=timezone.now()).order_by('data_publi')
    return render(request, 'base.html', {'posts': posts})