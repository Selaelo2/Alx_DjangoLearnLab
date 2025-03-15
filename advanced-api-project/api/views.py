# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

# ListView: List all books
class BookList(generics.ListAPIView):
    """
    API view to list all books.
    GET: Retrieve all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can add a book

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
    """
    API view to update a book by ID.
    PUT/PATCH: Update a book by ID (only for authenticated users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update a book

# DeleteView: Delete a book by ID
class BookDelete(generics.DestroyAPIView):
    """
    API view to delete a book by ID.
    DELETE: Delete a book by ID (only for authenticated users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete a book
