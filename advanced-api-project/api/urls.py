from django.urls import path
from .views import (
    AuthorListAPI, AuthorDetailAPI,
    BookListAPI, BookDetailAPI,
    BookCreateAPI, BookUpdateAPI, BookDeleteAPI,
)

urlpatterns = [
    path("authors/", AuthorListAPI.as_view(), name="authors-list"),
    path("authors/<int:pk>/", AuthorDetailAPI.as_view(), name="authors-detail"),

    path("books/", BookListAPI.as_view(), name="books-list"),
    path("books/<int:pk>/", BookDetailAPI.as_view(), name="books-detail"),
    path("books/create/", BookCreateAPI.as_view(), name="books-create"),
    path("books/<int:pk>/update/", BookUpdateAPI.as_view(), name="books-update"),
    path("books/<int:pk>/delete/", BookDeleteAPI.as_view(), name="books-delete"),
]
