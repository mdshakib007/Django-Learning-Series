from django.urls import path
from post import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('category/<slug:category_slug>/', views.home_view, name='category_wise_post'),
    path('create/', views.create_post_view, name='create_post'),
    path('post/<int:id>', views.single_post_view, name='single_post'),
    path('author/<str:username>/post/<int:id>/edit', views.edit_post_view, name='edit_post'),
    path('author/<str:username>/post/<int:id>/delete', views.delete_post_view, name='delete_post'),
]

