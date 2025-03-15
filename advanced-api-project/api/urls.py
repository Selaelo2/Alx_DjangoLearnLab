# api/urls.py
from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/create/', BookCreate.as_view(), name='book-create'),  # Create a new book
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),  # Retrieve a specific book
    path('books/<int:pk>/update/', BookUpdate.as_view(), name='book-update'),  # Update a specific book
    path('books/<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),
]
