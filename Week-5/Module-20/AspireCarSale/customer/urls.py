from django.urls import path
from customer import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'), # Class based view
    path('login/', views.CustomerLoginView.as_view(), name='login'), # class Based Vieww
    path('logout/', views.logout_view, name='logout'),
    path('customer/<str:username>/', views.profile_view, name='profile'),
    path('customer/<str:username>/edit/', views.edit_profile_view, name='edit_profile'),
    path('customer/<str:username>/change-password/', views.change_password_view, name='change_password'),
]
