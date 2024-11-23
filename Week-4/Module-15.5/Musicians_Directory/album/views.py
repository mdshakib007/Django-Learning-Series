from django.shortcuts import render, redirect
from album.forms import AlbumForm
from album.models import AlbumModel

# Create your views here.
def add_album(request):
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_album')
    return render(request, 'album/add_album.html', {'form' : form})


def edit_album(request, id):
    alb = AlbumModel.objects.get(pk=id)
    form = AlbumForm(instance=alb)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=alb)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'album/add_album.html', {'form' : form})


def delete_album(request, id):
    AlbumModel.objects.get(pk=id).delete()
    return redirect('home')