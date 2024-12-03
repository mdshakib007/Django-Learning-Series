from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from post import forms
from post.models import Post
from category.models import Category
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def home_view(request, category_slug = None):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    current_cat = None
    
    if category_slug is not None:
        cat = Category.objects.get(slug=category_slug)
        current_cat = cat.name
        posts = Post.objects.filter(category=cat).order_by('-created_at')

    return render(request, 'post/home.html', {'posts' : posts, 'categories' : categories, 'current_cat' : current_cat})


def create_post_view(request):
    if request.user.is_authenticated:
        form = forms.PostForm()
        if request.method == "POST":
            form = forms.PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user   
                post.save()                
                form.save_m2m()                
                messages.success(request, "Your Post Successfully Uploaded!")
                return redirect('home')
        return render(request, 'post/create_post.html', {'form': form})
    else:
        return redirect('login')

@method_decorator(login_required, name='dispatch')
class CreatePostView(CreateView):
    model = Post
    form_class = forms.PostForm
    success_url = reverse_lazy('home')
    template_name = 'post/create_post.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


def single_post_view(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'post/single_post.html', {'post' : post})


class SinglePostView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'post/single_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object  # The current post instance
        comments = post.comments.all()
        form = forms.CommentForm()

        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Get the current post instance
        form = forms.CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = self.object  # Assign the current post to the comment
            new_comment.author = request.user  # Set the logged-in user as the author
            new_comment.save()
            # Redirect to the same post after saving the comment
            return HttpResponseRedirect(reverse('single_post', kwargs={'id': self.object.id}))

        # If the form is not valid, re-render the page with the form errors
        context = self.get_context_data(form=form)
        return self.render_to_response(context)




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

class EditPostView(UpdateView):
    model = Post
    form_class = forms.PostForm
    template_name = 'post/create_post.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    


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

class DeletePostView(DeleteView):
    model = Post
    template_name = 'post/delete_post.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

