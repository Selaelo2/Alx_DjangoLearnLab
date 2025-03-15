# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Query to fetch all books
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data
