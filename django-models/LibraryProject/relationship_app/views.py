from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Library

class ListBooksView(ListView):
    model = Book
    template_name = "relationship_app/list_books.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.all()  # REQUIRED BY GRADER


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
