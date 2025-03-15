# api/urls.py

from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Define the route to your BookList view
]


# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Include the router's URLs for CRUD operations
    path('', include(router.urls)),
]
