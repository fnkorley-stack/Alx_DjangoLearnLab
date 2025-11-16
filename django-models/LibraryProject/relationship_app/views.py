from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Library

# Function-based view required by the task
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based ListView (also satisfies the “simple text list” requirement)
class ListBooksView(ListView):
    model = Book
    template_name = "relationship_app/list_books.html"
    context_object_name = "books"

# Class-based DetailView for Library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
