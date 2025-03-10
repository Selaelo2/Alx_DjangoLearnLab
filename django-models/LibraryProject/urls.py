
from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
     path('books/', list_books, name='list_books'),  
    path('relationship/', include('relationship_app.urls')),  
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
     path('register/', register, name='register'), 
    path('login/', CustomLoginView.as_view(), name='login'), 
    path('logout/', CustomLogoutView.as_view(), name='logout'), 
]

