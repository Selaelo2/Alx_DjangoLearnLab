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
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Admin view - Only accessible to users with the 'Admin' role
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Utility function to check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Utility function to check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view - Only accessible to users with the 'Admin' role
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view - Only accessible to users with the 'Librarian' role
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view - Only accessible to users with the 'Member' role
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
