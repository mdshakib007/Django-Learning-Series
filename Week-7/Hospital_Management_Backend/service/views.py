from django.shortcuts import render
from service.serializers import ServiceSerializer
from service.models import Service
from rest_framework import viewsets

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer