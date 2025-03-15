from django.shortcuts import render

# Create your views here.
# bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.http import HttpResponseForbidden

# View to display a list of books (can be accessed by users with 'can_view' permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'book_list.html', {'books': books})  # Pass the books to the template

# View to display a book (requires 'can_view' permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'view_book.html', {'book': book})

# View to create a book (requires 'can_create' permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        publish_date = request.POST['publish_date']
        Book.objects.create(title=title, author=author, description=description, publish_date=publish_date)
        return redirect('book_list')  # Redirect to the book list view after creation
    return render(request, 'create_book.html')

# View to edit a book (requires 'can_edit' permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.description = request.POST['description']
        book.publish_date = request.POST['publish_date']
        book.save()
        return redirect('book_list')  # Redirect to the book list after editing
    return render(request, 'edit_book.html', {'book': book})

# View to delete a book (requires 'can_delete' permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')  # Redirect to the book list after deletion

# bookshelf/views.py

from django.shortcuts import render, redirect
from .forms import ExampleForm  # This is the import you need to add
from .models import Book

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Save data or process it as needed
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            description = form.cleaned_data['description']
            
            # Optionally, save this data into the Book model
            Book.objects.create(title=title, author=author, description=description)

            return redirect('book_list')  # Redirect to book list or another view after form submission
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/example_form.html', {'form': form})


