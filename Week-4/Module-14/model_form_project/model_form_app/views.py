from django.shortcuts import render, redirect
from . import models
from . import forms

# Create your views here.
def home(request):
    student = models.StudentModel.objects.all()
    return render(request, 'index.html', {'student' : student})

def delete_student(request, roll):
    std = models.StudentModel.objects.get(pk=roll).delete()
    return redirect("home")
    
def form(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = forms.StudentForm()
    return render(request, 'form.html', {'form' : form})