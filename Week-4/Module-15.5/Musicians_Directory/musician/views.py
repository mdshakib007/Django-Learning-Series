from django.shortcuts import render, redirect
from musician.forms import MusicianForm
from musician.models import MusicianModel

# Create your views here.
def add_musician(request):
    form = MusicianForm()
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        form.save()
        return redirect('add_musician')
    return render(request, 'musician/add_musician.html', {'form' : form})


def edit_musician(request, id):
    m = MusicianModel.objects.get(pk = id)
    form = MusicianForm(instance=m)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=m)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'musician/add_musician.html', {'form' : form})