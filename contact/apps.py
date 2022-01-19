"""Configuration file"""
from django.apps import AppConfig

# app configuration
class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
