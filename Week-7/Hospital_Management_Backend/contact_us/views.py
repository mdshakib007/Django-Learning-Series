from django.shortcuts import render
from rest_framework import viewsets
from contact_us.serializers import ContactUsSerializer
from contact_us.models import ContactUs

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
