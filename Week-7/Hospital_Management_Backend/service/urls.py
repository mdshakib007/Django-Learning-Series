from django.urls import path, include
from rest_framework.routers import DefaultRouter
from service.views import ServiceViewSet

router = DefaultRouter()
router.register('services', ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
