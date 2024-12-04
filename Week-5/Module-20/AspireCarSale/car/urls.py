from django.urls import path
from car import views

urlpatterns = [
    path('<int:id>/details/', views.view_details_view, name='view_details'),
    path('<int:id>/order/', views.confirm_order_view, name='confirm_order'),
]
