from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Define the choices for user roles
    USER_ROLES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    # One-to-one relationship with the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Role field with choices for 'Admin', 'Librarian', and 'Member'
    role = models.CharField(max_length=10, choices=USER_ROLES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Django signal to automatically create or update the UserProfile when a new user is registered
from django.db.models.signals import post_save
from django.dispatch import receiver

# Signal to create or update UserProfile when a User is saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    This function creates or updates the UserProfile when a User instance is created or updated.
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()


from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ('can_add_book', 'Can add new book'),
            ('can_change_book', 'Can edit book details'),
            ('can_delete_book', 'Can delete book'),
        ]
    
    def __str__(self):
        return self.title
