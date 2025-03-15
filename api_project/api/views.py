

# api/views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Query to fetch all books
    serializer_class = BookSerializer  # Serializer to convert book data to JSON format
