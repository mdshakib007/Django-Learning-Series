from django.urls import path
from author import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/<str:username>/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/<str:username>/change-password/', views.change_password_view, name='change_password'),
]
