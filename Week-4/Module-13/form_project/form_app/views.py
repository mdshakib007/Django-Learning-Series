from django.shortcuts import render
from . import forms

# Create your views here.
def registration(request):
    return render(request, 'registration.html')

def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html', {'name' : name, 'email':email, 'select' : select})
    return render(request, 'about.html')

def django_form(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./form_app/upload/'+ file.name, 'wb+') as dest:
                for chunk in file.chunks():
                    dest.write(chunk)
            print(form.cleaned_data)
    else:
        form = forms.ContactForm()
    return render(request, 'django_form.html', {'form': form})
        
def student_form(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = forms.StudentForm()
    return render(request, 'student_form.html', {'form' : form})

def login(request):
    if request.method == 'POST':
        form = forms.Login(request.POST)
        if(form.is_valid()):
            print(form.cleaned_data)
    else: form = forms.Login()
    return render(request, 'login.html', {'form': form})