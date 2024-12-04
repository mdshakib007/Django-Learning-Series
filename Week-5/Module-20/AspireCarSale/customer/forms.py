from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class RegistrationForm(UserCreationForm):
    usable_password = None
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        for field in fields:
            self.fields[field].help_text = None
            self.fields[field].widget.attrs.update({'required': True})

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class EditProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'required'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].help_text = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

