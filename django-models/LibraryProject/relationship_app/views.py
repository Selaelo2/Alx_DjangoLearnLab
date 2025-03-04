from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

# Register View: Handle user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Automatically log in the user after registration
            username = form.cleaned_data.get('username')
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login View: Use Django's built-in login view
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout View: Use Django's built-in logout view
class CustomLogoutView(LogoutView):
    next_page = '/'  # Redirect to homepage after logout
