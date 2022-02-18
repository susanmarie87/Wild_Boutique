"""Form receives user information"""
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """A view to receive user information"""
    class Meta:
        """Meta class defines how contact information will behave"""
        model = Contact
        fields = '__all__'
