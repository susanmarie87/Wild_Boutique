"""A view to return the contact page"""
from django.shortcuts import render

# Create your views here.


def contact(request):
    return render(request, 'contact.html')
