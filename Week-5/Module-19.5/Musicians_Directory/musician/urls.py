from django.urls import path
from musician import views

urlpatterns = [
    path('add/', views.AddMusician.as_view(), name='add_musician'),
    path('edit/<int:id>', views.EditMusician.as_view(), name='edit_musician'),
]
