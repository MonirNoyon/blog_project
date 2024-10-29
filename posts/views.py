from django.shortcuts import render, redirect
from .import forms
from .import models
from .models import Post
from django.db.models import Q

def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})


def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    
    return redirect ('homepage')

def search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.all()
    return render(request, 'base.html', {'posts': posts, 'query': query})

