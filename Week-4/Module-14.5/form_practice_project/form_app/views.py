from django.shortcuts import render
from form_app import forms

# Create your views here.
def django_form(request):
    dj_form = forms.DjangoForm()
    return render(request, 'form_app/django_form.html', {'form' : dj_form})

def model_form(request):
    md_form = forms.MDForm()
    return render(request, 'form_app/model_form.html', {'form':md_form})