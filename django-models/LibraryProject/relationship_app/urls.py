from django.contrib import admin
from django.urls import path, include  # include is required to include the app URLs
from .views import list_books, LibraryDetailView, register, user_login, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),  # Include the relationship app URLs
      path('books/', list_books, name='list_books'),  # Function-based view for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
    path('register/', register, name='register'),  # Registration view
    path('login/', user_login, name='login'),  # Login view
    path('logout/', user_logout, name='logout'),  # Logout view
]
