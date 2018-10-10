from django.shortcuts import render
from django.utils import timezone
from .models import Post, PeR
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, PERForm
from events.models import Event
from django.utils.timezone import localdate
from datetime import datetime


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {
        'events': Event.objects.filter(
            date='{:%Y-%m-%d}'.format(day)).order_by('-priority', 'event'),
        'form': form

    }
    return render(request, 'blog/post_edit.html', context)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form' : form})

def per(request):
    post = get_object_or_404(Post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/per.html', {'form' : form})

def per_list(request):
    pers = PeR.objects.all()
    return render(request, 'blog/per_list.html', {'pers': pers})

def per_new(request):
    if request.method == 'PER':
        form = PERForm(request.PER)
        if form.is_valid():
            per = form.save(commit=False)
            per.nome = request.user
            per.deh_publi = timezone.now()
            per.save()
            return redirect('per_detail')
    else:
        form = PERForm()

    context = {
        'form': form
    }
    return render(request, 'blog/per_edit.html', context)