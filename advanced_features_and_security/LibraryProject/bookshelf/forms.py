# bookshelf/forms.py

from django import forms
from .models import Book

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=255, required=True, label="Book Title")
    author = forms.CharField(max_length=255, required=True, label="Author")
    description = forms.CharField(widget=forms.Textarea, required=True, label="Description")
    
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
