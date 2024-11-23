from django import forms
from django.core import validators
from form_app import models

class DjangoForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), max_length=20, initial="Shakib")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'id' : 'about', 'class' : 'form-control', 'placeholder': 'Enter your short info here...', }))
    age = forms.CharField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    weight = forms.FloatField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    balance = forms.DecimalField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date', 'class' : 'form-control'}))
    appoinment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local', 'class' : 'form-control'}))
    RATING = [('1', 'One'), ('2', 'Two'), ('3', 'Three')]
    Rating = forms.ChoiceField(choices=RATING, widget=forms.RadioSelect())
    GAMES = [('football', 'FootBall'), ('cricket', 'Cricket'), ('hockey', 'Hockey')]
    Games = forms.MultipleChoiceField(choices=GAMES, widget=forms.CheckboxSelectMultiple())
    file = forms.FileField(required=False)
    check = forms.BooleanField(label="Agree our Terms & Conditions")
    COLORS = [('1', 'Black'), ('2', 'Green'), ('3', 'Blue')]
    colors = forms.ChoiceField(choices=COLORS)



class MDForm(forms.ModelForm):
    
    class Meta:
        model = models.MDModel
        fields = '__all__'

        labels = {
            'name' : 'Your Name',
            'email' : 'Your Email',
            'boolean_field' : 'Accept Terms & Conditions'
        }
