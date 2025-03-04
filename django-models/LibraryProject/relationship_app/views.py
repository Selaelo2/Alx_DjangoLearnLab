from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Function-based view for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Function-based view for user login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('list_books')  # Redirect to books list after login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Function-based view for user logout
def user_logout(request):
    logout(request)  # Logs the user out
    return redirect('login')  # Redirect to login page after logging out


# Utility function to check if the user is an Admin
# Utility function to check if the user is an Admin
class UserProfile(models.Model):
    # Define choices for user roles
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

# Django signal to automatically create or update the UserProfile when a User is created/updated
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
    # Save the UserProfile instance whenever the User instance is updated
    instance.userprofile.save()