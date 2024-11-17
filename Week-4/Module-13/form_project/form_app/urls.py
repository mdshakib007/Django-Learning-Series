from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name = 'registration'),
    path('login/', views.login, name='login'),
    path('django_form/', views.django_form, name='django_form'),
    path('student_form/', views.student_form, name='student_form'),
    path('about/', views.about, name='about'),
]

