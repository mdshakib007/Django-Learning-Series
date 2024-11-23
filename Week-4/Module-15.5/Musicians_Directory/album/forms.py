from django import forms
from album.models import AlbumModel

class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = AlbumModel
        exclude = ['release_date']

