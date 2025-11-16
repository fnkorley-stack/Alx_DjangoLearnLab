from django.urls import path
from .views import list_books, ListBooksView, LibraryDetailView

urlpatterns = [
    path('books/', ListBooksView.as_view(), name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('books-function/', list_books, name='books_function'),
]
