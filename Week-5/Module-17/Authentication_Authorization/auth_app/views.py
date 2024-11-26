from django.shortcuts import render, redirect
from auth_app import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash



def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        form = forms.SignUpForm()
        if request.method == 'POST':
            form = forms.SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Successfully Created!")
                
        return render(request, 'signup.html', {'form' : form})

def log_in(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        form = AuthenticationForm()
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username=name, password = user_pass)
                
                if user is not None:
                    login(request, user)
                    return redirect('profile')

        return render(request, 'login.html', {'form' : form})


def profile(request):
    if request.user.is_authenticated:
        form = forms.ChangeUserData(instance=request.user)
        if request.method == 'POST':
            form = forms.ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Information Updated Successfully!")
        return render(request, 'profile.html', {'form' : form})
    else:
        return redirect('login')


def log_out(request):
    logout(request)
    return redirect('login')

def change_password(request):
    if request.user.is_authenticated:
        form = PasswordChangeForm(request.user)
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        
        return render(request, 'change_password.html', {'form' : form})
    else:
        return redirect('login')

def change_password2(request):
    if request.user.is_authenticated:
        form = SetPasswordForm(request.user)
        if request.method == 'POST':
            form = SetPasswordForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        
        return render(request, 'change_password.html', {'form': form})
    else:
        return redirect('login')
    
