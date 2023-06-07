from distutils.command.upload import upload
from django import forms
from django.contrib.auth import get_user_model
from captcha.fields import CaptchaField
from .models import Contact

User = get_user_model()

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control", 
            "placeholder": "Enter your First Name"
        }))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Enter your Last Name"
        }))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Enter your phone number"
        }))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Email"
        }))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Enter your message",
            "rows" : "5",
        }),
            max_length=2000
        )
    # image = forms.FileInput()
    # image = forms.ImageField()
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ['first_name','last_name','phone','email','message','image','captcha']
