# api/urls.py
from django.urls import path
from .views import BookList, BookCreate, BookDetail, BookUpdate, BookDelete

urlpatterns = [
    # List all books
    path('books/', BookList.as_view(), name='book-list'),

    # Create a new book
    path('books/create/', BookCreate.as_view(), name='book-create'),

    # Retrieve a specific book by ID
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),

    # Update a specific book (with the book's ID)
    path('books/<int:pk>/update/', BookUpdate.as_view(), name='book-update'),

    # Delete a specific book (with the book's ID)
    path('books/<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),
]
