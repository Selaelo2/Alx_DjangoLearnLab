from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Author, Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters  # Correct import for filters
from rest_framework import generics

# Author Views
class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'  # Template for listing authors
    context_object_name = 'authors'
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access to unauthenticated

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'  # Template for author details
    context_object_name = 'author'
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticatedOrReadOnly] 
    filter_backends = [filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  # Correctly includes OrderingFilter
    filterset_class = BookFilter  # Use the custom filter class
    search_fields = ['title', 'author__name']  # Fields to search
    ordering_fields = ['title', 'publication_year']  # Fields to order by
    ordering = ['title']  # Default ordering

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'  # Template for book details
    context_object_name = 'book'
    permission_classes = [IsAuthenticated]

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

    class BookFilter(filters.FilterSet):
        title = filters.CharFilter(lookup_expr='icontains')  # Case-insensitive partial match
        author__name = filters.CharFilter(lookup_expr='icontains')  # Filter by author name
        publication_year = filters.NumberFilter()  # Exact match for publication year
    
        class Meta:
            model = Book
            fields = ['title', 'author__name', 'publication_year']