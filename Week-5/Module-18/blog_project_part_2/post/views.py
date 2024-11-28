from django.shortcuts import render, redirect
from post import forms
from post.models import Post
from django.contrib import messages


def home_view(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post/home.html', {'posts' : posts})


def create_post_view(request):
    if request.user.is_authenticated:
        form = forms.PostForm()
        if request.method == "POST":
            form = forms.PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request, "Your Post Successfully Uploaded!")
                return redirect('home')
        return render(request, 'post/create_post.html', {'form' : form})
    else:
        return redirect('login')


def single_post_view(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'post/single_post.html', {'post' : post})


def edit_post_view(request, username, id):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=id)
        if post.author.username != username:
            return redirect('home')
        
        form = forms.PostForm(instance=post)
        if request.method == 'POST':
            form = forms.PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, "Post Updated Successfully!")
                return redirect('profile', username=username)
        return render(request, 'post/create_post.html', {'form' : form})


def delete_post_view(request, username, id):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=id)
        if post.author.username != username:
            return redirect('home')
        post.delete()
        messages.success(request, "Post Deleted Successfully!")
        return redirect('profile', username=username) 
    else:
        return redirect('login')