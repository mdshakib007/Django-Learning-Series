from django.shortcuts import render, redirect
from album.forms import AlbumForm
from album.models import AlbumModel
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def add_album(request):
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_album')
    return render(request, 'album/add_album.html', {'form' : form})

class AddAlbum(CreateView):
    template_name = 'album/add_album.html'
    model = AlbumModel
    form_class = AlbumForm
    success_url = reverse_lazy('add_album')

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)   




def edit_album(request, id):
    alb = AlbumModel.objects.get(pk=id)
    form = AlbumForm(instance=alb)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=alb)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'album/add_album.html', {'form' : form})

class EditAlbum(UpdateView):
    template_name = 'album/add_album.html'
    model = AlbumModel
    form_class = AlbumForm
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'



def delete_album(request, id):
    AlbumModel.objects.get(pk=id).delete()
    return redirect('home')

class DeleteAlbum(DeleteView):
    success_url = reverse_lazy('home')
    model = AlbumModel
    pk_url_kwarg = 'id'
    template_name = 'album/confirm_delete.html'
    success_url = reverse_lazy('home')