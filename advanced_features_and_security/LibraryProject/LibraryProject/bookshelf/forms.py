# bookshelf/forms.py

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    # You can define custom fields or modify the ModelForm here
    title = forms.CharField(max_length=255, required=True)
    author = forms.CharField(max_length=255, required=True)
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']  # Ensure this matches your model's fields

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters.")
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if len(author) < 3:
            raise forms.ValidationError("Author name must be at least 3 characters.")
        return author
