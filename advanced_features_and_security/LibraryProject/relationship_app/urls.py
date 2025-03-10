from django import views
from django.contrib import admin
from django.urls import path, include  # include is required to include the app URLs
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),  # Include the relationship app URLs
      path('books/', list_books, name='list_books'),  # Function-based view for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
    path('register/', views.register, name='register'),  # Registration view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout view
    path('add/', views.add_book, name='add_book'),

    # URL for editing a book (requires permission 'can_change_book')
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),

    # URL for deleting a book (requires permission 'can_delete_book')
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]
