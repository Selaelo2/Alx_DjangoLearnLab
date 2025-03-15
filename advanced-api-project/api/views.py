# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

# List View
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can list or create

# Detail View
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    # api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

# ListView: List all books
class BookList(generics.ListCreateAPIView):
    """
    API view to list all books or create a new book.
    GET: Retrieve all books.
    POST: Create a new book (only for authenticated users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create a book

# DetailView: Retrieve a single book by ID
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a book by ID.
    GET: Retrieve a book by ID.
    PUT/PATCH: Update a book by ID.
    DELETE: Delete a book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can modify or delete a book

