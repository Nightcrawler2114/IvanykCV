from django import forms
from .models import ContactFace


class ContactMe(forms.ModelForm):
    class Meta:
        model = ContactFace
        exclude = ['']