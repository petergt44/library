from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author, UserFavorite

class BookAPITests(APITestCase):
    """Test suite for Book API"""

    def setUp(self):
        """Setup initial test data and user authentication"""
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='J.K. Rowling', biography='Famous author')
        self.book = Book.objects.create(title='Harry Potter', author=self.author, published_date='2000-01-01')

        self.client.login(username='testuser', password='testpass')

    def test_get_books(self):
        """Test to retrieve a list of all books"""
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        """Test book creation (protected)"""
        data = {
            'title': 'New Book',
            'author': self.author.id,
            'published_date': '2024-01-01'
        }
        response = self.client.post(reverse('book-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_search_books(self):
        """Test search functionality to find books by title or author name"""
        response = self.client.get(reverse('book-list') + '?search=Harry')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_recommendations(self):
        """Test book recommendation endpoint"""
        UserFavorite.objects.create(user=self.user, book=self.book)
        response = self.client.get(reverse('book-recommendations'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AuthorAPITests(APITestCase):
    """Test suite for Author API"""

    def test_get_authors(self):
        """Test to retrieve a list of all authors"""
        response = self.client.get(reverse('author-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
