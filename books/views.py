from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q

from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .models import Book, Author, UserFavorite
from .serializers import BookSerializer, AuthorSerializer, UserFavoriteSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Books.

    Supports the following actions:
    - GET: List all books or filter by search query (search by title or author).
    - POST: Create a new book (authenticated users only).
    - PUT: Update an existing book (authenticated users only).
    - DELETE: Delete a book (authenticated users only).
    
    Also includes a custom action `recommendations` to suggest books not already marked as a favorite.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Optionally filters the books by a search query.

        The search allows filtering by book title or author name.

        Returns:
            QuerySet: Filtered set of books based on the search query.
        """
        query = self.request.query_params.get('search', None)
        if query:
            return self.queryset.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
        return self.queryset

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def recommendations(self, request):
        """
        Provides book recommendations based on the user's favorite list.

        Excludes books already in the user's favorite list and suggests up to 5 books.

        Returns:
            Response: List of recommended books serialized in JSON format.
        """
        user = request.user
        favorites = UserFavorite.objects.filter(user=user).values_list('book_id', flat=True)
        recommended_books = Book.objects.exclude(id__in=favorites)[:5]
        serializer = BookSerializer(recommended_books, many=True)
        return Response(serializer.data)


class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Authors.

    Supports the following actions:
    - GET: List all authors.
    - POST: Create a new author (authenticated users only).
    - PUT: Update an existing author (authenticated users only).
    - DELETE: Delete an author (authenticated users only).
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class UserFavoriteViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing user favorite books.

    Allows users to add/remove books from their favorite list.
    - GET: List of favorite books for the authenticated user.
    - POST: Add a new book to the user's favorite list.
    - DELETE: Remove a book from the user's favorite list.
    """
    serializer_class = UserFavoriteSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Returns the list of books marked as favorite by the authenticated user.

        Returns:
            QuerySet: The favorite books for the user.
        """
        return UserFavorite.objects.filter(user=self.request.user)


class RegisterView(APIView):
    """
    View for user registration.

    Allows new users to register by providing a username and password.
    On successful registration, a JWT token pair (refresh and access) is returned.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Registers a new user.

        Args:
            request: The HTTP request object containing username and password.

        Returns:
            Response: JWT token pair (refresh and access).
        """
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(username=username, password=password)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class LoginView(APIView):
    """
    View for user login.

    Authenticates users by verifying their username and password.
    On successful login, a JWT token pair (refresh and access) is returned.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Authenticates a user and returns a JWT token pair.

        Args:
            request: The HTTP request object containing username and password.

        Returns:
            Response: JWT token pair (refresh and access), or HTTP 401 if authentication fails.
        """
        username = request.data['username']
        password = request.data['password']
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
        except User.DoesNotExist:
            pass
        return Response(status=status.HTTP_401_UNAUTHORIZED)
