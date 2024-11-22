from django.shortcuts import render, redirect
from .forms import PostForm, Post

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    else:
        post_form = PostForm()
    return render(request, 'add_post.html', {'form' : post_form})


def edit_post(request, id):
    post = Post.objects.get(pk=id)
    edit_form = PostForm(instance=post)
    if request.method == 'POST':
        edit_form = PostForm(request.POST, instance=post)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('home')
    return render(request, 'add_post.html', {'form' : edit_form})


def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')