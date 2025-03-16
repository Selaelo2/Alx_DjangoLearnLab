from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()

        # Create a test author
        self.author = Author.objects.create(name='J.K. Rowling')

        # Create a test book
        self.book = Book.objects.create(
            title='Harry Potter',
            publication_year=1997,
            author=self.author
        )

        # Authenticate the test user
        self.client.force_authenticate(user=self.user)

    def test_create_book(self):
        """
        Ensure we can create a new book.
        """
        url = reverse('book-list')
        data = {
            'title': 'The Hobbit',
            'publication_year': 1937,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, 'The Hobbit')

    def test_retrieve_book(self):
        """
        Ensure we can retrieve a book.
        """
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Harry Potter')

    def test_update_book(self):
        """
        Ensure we can update a book.
        """
        url = reverse('book-detail', args=[self.book.id])
        data = {
            'title': 'Harry Potter and the Sorcerer\'s Stone',
            'publication_year': 1998,
            'author': self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Harry Potter and the Sorcerer\'s Stone')

    def test_delete_book(self):
        """
        Ensure we can delete a book.
        """
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        """
        Ensure we can filter books by title.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'title': 'Harry Potter'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Harry Potter')

    def test_search_books(self):
        """
        Ensure we can search books by title or author name.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Rowling'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Harry Potter')

    def test_order_books_by_publication_year(self):
        """
        Ensure we can order books by publication year.
        """
        # Create another book for testing ordering
        Book.objects.create(
            title='The Lord of the Rings',
            publication_year=1954,
            author=self.author
        )

        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'The Lord of the Rings')
        self.assertEqual(response.data[1]['title'], 'Harry Potter')

    def test_unauthenticated_access(self):
        """
        Ensure unauthenticated users cannot access protected endpoints.
        """
        self.client.logout()  # Log out the authenticated user
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)