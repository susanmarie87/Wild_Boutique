"""Import contact models and register"""
from django.contrib import admin
from .models import Contact

admin.site.register(Contact)
