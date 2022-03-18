from pyexpat import model
from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'sender', 'email', 'detail']