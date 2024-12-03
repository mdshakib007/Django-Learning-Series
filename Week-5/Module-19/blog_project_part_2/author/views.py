from django.shortcuts import render, redirect
from author import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from post.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

def profile_view(request, username):
    if request.user.is_authenticated:
        if request.user.username != username:
            return redirect('home')

        user = User.objects.get(username=username)
        posts = Post.objects.filter(author=user).order_by('-created_at')
        return render(request, 'author/profile.html', {'user' : user, 'posts' : posts})

    else:
        return redirect('login')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = AuthenticationForm()
        
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Login Successfull. Welcome, {username}!")
                    return redirect('home')

        return render(request, 'author/login.html', {'form' : form})

class UserLoginView(LoginView):
    template_name = 'author/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, f"Login Successfull.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = forms.RegistrationForm()

        if request.method == 'POST':
            form = forms.RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, f"Registration Successfull. Welcome, {user.username}!")
                return redirect('home')

        return render(request, 'author/register.html', {'form' : form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')



def edit_profile_view(request, username):
    if request.user.is_authenticated:
        if request.user.username != username:
            return redirect('home')

        form = forms.ChangeInformation(instance=request.user)
        if request.method == 'POST':
            form = forms.ChangeInformation(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile Information Updated Successfully!")
                return redirect('profile', username=form.instance.username)

        return render(request, 'author/edit_profile.html', {'form': form})

    else:
        return redirect('login')


def change_password_view(request, username):
    if request.user.is_authenticated:
        if request.user.username != username:
            return redirect('home')

        form = PasswordChangeForm(request.user)
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Password Updated Successfully!")
                return redirect('profile', username=username)

        return render(request, 'author/change_password.html', {'form' : form})

    else:
        return redirect('login')