from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=128, help_text='Enter a valid email.')
    username = models.CharField(max_length=24, help_text='<li>Must be less than 24 characters long.<li>Must not have been already taken.')
    password = models.CharField(max_length=128, help_text='<li>Must be more than 8 characters.<li>Cannot be a commonly used password.<li>Cannot be entirely numeric.')

    REQUIRED_FIELDS = [username, password]
