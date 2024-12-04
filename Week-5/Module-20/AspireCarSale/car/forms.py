from django import forms
from car.models import CommentModel

class CommentBox(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['body']
        widgets = {
            'body' : forms.Textarea(attrs={'placeholder' : "Leave a Comment..."})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].label = 'Add a Comment...'
