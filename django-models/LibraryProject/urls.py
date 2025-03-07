"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
     path('books/', list_books, name='list_books'),  # Route for function-based view
    path('relationship/', include('relationship_app.urls')),  # Include relationship_app URLs
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Route for class-based view
     path('register/', register, name='register'),  # Registration view
    path('login/', CustomLoginView.as_view(), name='login'),  # Login view
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Logout view
]

