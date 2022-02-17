"""Configuration file"""
from django.apps import AppConfig


class BagConfig(AppConfig):
    """Django Database models"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
