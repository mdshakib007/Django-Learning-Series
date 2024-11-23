from django.urls import path
from form_app import views

urlpatterns = [
    path('django_form/', views.django_form),
    path('model_form/', views.model_form)
]

