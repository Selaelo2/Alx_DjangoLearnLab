from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"
    

    
    # bookshelf/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager  # Import the custom manager

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()  # Use the custom manager

    def __str__(self):
        return self.username



