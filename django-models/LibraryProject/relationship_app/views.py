from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

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

# View for Admin users
@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    return HttpResponse('Welcome, Admin!')

# View for Librarian users
@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    return HttpResponse('Welcome, Librarian!')

# View for Member users
@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    return HttpResponse('Welcome, Member!')
