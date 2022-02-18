"""Contact form models"""
from django.db import models


class Contact(models.Model):
    """Manages contact form data"""
    first_name = models.CharField(max_length=72)
    last_name = models.CharField(max_length=72)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return str(self.email)
