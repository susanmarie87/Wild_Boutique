from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=72)
    last_name = models.CharField(max_length=72)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return str(self.email)
