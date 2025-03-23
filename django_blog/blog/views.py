from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import Profile

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            return render(request, "blog/login.html", {"error": "Invalid credentials"})
    return render(request, "blog/login.html")

@login_required
def update_profile(request):
    profile = Profile.objects.get_or_create(user=request.user)[0]
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "blog/update_profile.html", {"form": form})