# api/serializers.py
from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation to ensure the publication_year is not in the future
    def validate_publication_year(self, value):
        if value > 2025:  # You can change 2025 to the current year
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
        # api/serializers.py

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.
    Converts Book instances to JSON and validates the publication year.
    """
    def validate_publication_year(self, value):
        """
        Ensures that the publication year is not in the future.
        """
        if value > 2025:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model.
    Includes a nested BookSerializer to represent the books written by the author.
    """
    books = BookSerializer(many=True, read_only=True)  # Nested serializer to serialize related books


