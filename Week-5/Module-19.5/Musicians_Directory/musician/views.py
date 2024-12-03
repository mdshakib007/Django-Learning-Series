from django.shortcuts import render, redirect
from musician.forms import MusicianForm
from musician.models import MusicianModel
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
def add_musician(request):
    form = MusicianForm()
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        form.save()
        return redirect('add_musician')
    return render(request, 'musician/add_musician.html', {'form' : form})

class AddMusician(CreateView):
    template_name = 'musician/add_musician.html'
    success_url = reverse_lazy('add_musician')
    context_object_name = 'form'
    model = MusicianModel
    form_class = MusicianForm

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return self.render_to_response(self.get_context_data(form=form))
    
    


def edit_musician(request, id):
    m = MusicianModel.objects.get(pk = id)
    form = MusicianForm(instance=m)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=m)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'musician/add_musician.html', {'form' : form})

class EditMusician(UpdateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = 'musician/add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')