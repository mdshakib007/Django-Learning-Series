from django import forms
from django.core import validators

# Widgets --> Field to HTML Input
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    about = forms.CharField(widget=forms.Textarea(attrs={'id' : 'about', 'class' : 'about_class', 'placeholder': 'Enter your short info here...', }))
    age = forms.CharField(widget=forms.NumberInput())
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date', }))
    appoinment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local', }))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple())
    file = forms.FileField()


def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Ahh! info is too short!")
    else: return value

class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Your Name'}), validators=[validators.MinLengthValidator(4, "Your Name is too Small!"), validators.MaxLengthValidator(20, "Ahh! Too big Name!")])
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' : 'Your Email'}), validators=[validators.EmailValidator("Ahh! check your email! It's Wrong!")])
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder' : 'Your Age'}), validators=[validators.MinValueValidator(18, "Ahh! You Are a Child!")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(['pdf'], "Ahh! please chose a PDF File")])
    # custom validator
    info = forms.CharField(widget=forms.Textarea(attrs={'placeholder' : 'Enter your info...'}), validators=[len_check])

    ## painful approach!
    # def clean_name(self):
    #     val_name = self.cleaned_data['name']
    #     if len(val_name) < 4:
    #         raise forms.ValidationError("Enter a Name at least 4 Character!")
    #     else:
    #         return val_name

    # def clean_email(self):
    #     val_email = self.cleaned_data['email']
    #     if '.com' not in val_email:
    #         raise forms.ValidationError("Invalid Email Input!")
    #     else:
    #         return val_email


    ## Easy Approach!
    # def clean(self):
    #     cleaned_data = super().clean()
    #     val_name = self.cleaned_data['name']
    #     val_email = self.cleaned_data['email']
        
    #     if len(val_name) < 4:
    #         raise forms.ValidationError("Your Name must be at least 4 characters!")

    #     if '.com' not in val_email:
    #         raise forms.ValidationError("Your Email must contains .com")



class Login(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter Your Name"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Enter Your Password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Enter Confirm Password"}))

    def clean(self):
        cleaned_data = super().clean()
        val_name = self.cleaned_data['name']
        val_pass = self.cleaned_data['password']
        val_con_pass = self.cleaned_data['confirm_password']
        
        if len(val_name) < 4:
            raise forms.ValidationError("Name is too short!")
        
        if val_pass != val_con_pass:
            raise forms.ValidationError("Password didn't match!")


        

