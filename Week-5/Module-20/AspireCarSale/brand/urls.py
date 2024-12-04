from django.urls import path
from brand import views

urlpatterns = [
    path('<int:id>/profile', views.brand_profile_view, name='brand_profile'),
]
