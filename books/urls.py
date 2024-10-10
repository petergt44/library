from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, UserFavoriteViewSet, RegisterView, LoginView

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'favorites', UserFavoriteViewSet, basename='favorites')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
