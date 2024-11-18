from django import forms
from . import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.StudentModel

        fields = '__all__'
        labels = {
            'roll' : "Student Roll",
            'name' : "Student Name",
        }
        widgets = {
            'roll' : forms.NumberInput(attrs={'placeholder': 'Enter Your Roll'}),
            'name' : forms.TextInput(attrs={'placeholder' : 'Enter Your Name'}),
            'father_name' : forms.TextInput(attrs={'placeholder' : 'Enter Your Father\'s Name'}),
            'address' : forms.Textarea(attrs={'placeholder' : 'Enter Your Address Here...'})
        }
        help_texts = {
            'name' : 'Write your full name',
        }
        error_messages = {
            'roll' : {'required' : 'Your name is required!'},
        }
