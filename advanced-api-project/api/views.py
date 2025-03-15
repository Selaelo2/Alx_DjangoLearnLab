# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly  # Add this import
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend  # Import here
from django_filters.rest_framework import DjangoFilterBackend 
from django_filters import rest_framework
from rest_framework.filters import OrderingFilter


# ListView: List all books
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Setup for filtering, search, and ordering
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)  # Correctly including OrderingFilter
    filterset_fields = ['title', 'author', 'publication_year']  # Fields you want to allow for filtering
    search_fields = ['title', 'author']  # Fields that can be searched by
    ordering_fields = ['title', 'publication_year']  # Fields that can be ordered by
    ordering = ['title']  # Default ordering

# CreateView: Create a new book
class BookCreate(generics.CreateAPIView):
    """
    API view to create a new book.
    POST: Create a new book (only for authenticated users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create a book

# DetailView: Retrieve a single book by ID
class BookDetail(generics.RetrieveAPIView):
    """
    API view to retrieve a book by ID.
    GET: Retrieve a book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can retrieve a book

# UpdateView: Update an existing book
class BookUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 

# DeleteView: Delete a book by ID
class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete a book