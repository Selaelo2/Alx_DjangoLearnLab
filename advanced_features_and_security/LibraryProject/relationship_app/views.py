from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.http import HttpResponseForbidden

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

# View to add a new book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_year = request.POST.get("publication_year")
        
        # Create the new book
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect('book_list')
    return render(request, 'add_book.html')

# View to edit a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("publication_year")
        book.save()
        return redirect('book_list')
    
    return render(request, 'edit_book.html', {'book': book})

# View to delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    
    return render(request, 'delete_book.html', {'book': book})

