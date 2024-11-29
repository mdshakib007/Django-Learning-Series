from post import models
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content', 'category', 'image']

        labels = ''

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter title here'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your blog content...'}),
            'category': forms.CheckboxSelectMultiple(attrs={'type' : 'checkbox'}),
        }


