from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author, Book

# Author Views
class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'  # Template for listing authors
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'  # Template for author details
    context_object_name = 'author'

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_form.html'  # Template for creating an author
    fields = ['name']
    success_url = reverse_lazy('author-list')

class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author_form.html'  # Template for updating an author
    fields = ['name']
    success_url = reverse_lazy('author-list')

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'  # Template for deleting an author
    success_url = reverse_lazy('author-list')

# Book Views
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'  # Template for listing books
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'  # Template for book details
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'  # Template for creating a book
    fields = ['title', 'publication_year', 'author']
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_form.html'  # Template for updating a book
    fields = ['title', 'publication_year', 'author']
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'  # Template for deleting a book
    success_url = reverse_lazy('book-list')