from .models import Book, Author, Library


# 1. List all books in a library
def list_books_in_library(library_id):
    return Book.objects.filter(library__id=library_id)


# 2. Query all books by a specific author
def get_books_by_author(author_id):
    return Book.objects.filter(author__id=author_id)


# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_id):
    library = Library.objects.get(id=library_id)
    return library.librarian
