
from django import forms
from . models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # Tell the form exactly which fields to show the user
        fields = ['name', 'phone', 'category', 'email']
