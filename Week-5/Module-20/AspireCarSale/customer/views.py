from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from customer.forms import RegistrationForm, EditProfileForm
from car.models import CarModel
from django.urls import reverse_lazy
from django.contrib.auth.models import User


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

        return render(request, 'customer/login.html', {'form' : form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "You have been logged out.")
    else:
        messages.warning(request, "You were not logged in.")
    return redirect('login')



def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successfull!")
            return redirect('home')
    return render(request, 'customer/register.html', {'form' : form})


def profile_view(request, username):
    if request.user.is_authenticated:
        if username == request.user.username:
            cars = CarModel.objects.filter(customer=request.user)
            total_spent = sum(car.price for car in cars)
            return render(request, 'customer/profile.html', {'cars' : cars, 'total_spent' : total_spent})
        else:
            messages.error(request, "Invalid URL Found!")
            return redirect('profile', username=request.user.username)
    else:
        return redirect('login')


def edit_profile_view(request, username):
    if request.user.is_authenticated:
        if username==request.user.username:
            form = EditProfileForm(instance=request.user)
            if request.method == 'POST':
                form = EditProfileForm(request.POST, instance=request.user)
                if form.is_valid():
                    form.save()
                    messages.success(request, "All Changes are Saved!")
                    return redirect('profile', username=request.user.username)
            return render(request, 'customer/edit_profile.html', {'form' : form})
        else:
            messages.warning(request, "Invalid URL Found!")
            return redirect('home')
    else:
        return redirect('login')

def change_password_view(request, username):
    if request.user.is_authenticated:
        if username==request.user.username:
            form = PasswordChangeForm(request.user)
            if request.method == 'POST':
                form = PasswordChangeForm(request.user, data=request.POST)
                if form.is_valid():
                    form.save()
                    update_session_auth_hash(request, form.user)
                    messages.success(request, "Password Updated Successfully!")
                    return redirect('profile', username=username)
            return render(request, 'customer/change_password.html', {'form': form})
        else:
            messages.warning(request, "Invalid URL Found!")
            return redirect('home')
    else:
        return redirect('login')


# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ----- Here i replaced 2 view function by class based view --------
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------


class CustomerLoginView(LoginView):
    template_name = 'customer/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Login Successful!")
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class RegisterView(CreateView):
    template_name = 'customer/register.html'
    form_class = RegistrationForm
    model = User
    
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Registration Successful! Please Login to Continue!")
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
