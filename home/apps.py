"""Application Configuration"""
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """Instance of app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
