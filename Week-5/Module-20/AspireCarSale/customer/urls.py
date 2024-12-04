from django.urls import path
from customer import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('customer/<str:username>/', views.profile_view, name='profile'),
    path('customer/<str:username>/edit/', views.edit_profile_view, name='edit_profile'),
    path('customer/<str:username>/change-password/', views.change_password_view, name='change_password'),
]
