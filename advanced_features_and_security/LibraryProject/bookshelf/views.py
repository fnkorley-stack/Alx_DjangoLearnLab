# bookshelf/views.py

from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm  # Import the secure search form


def book_list(request):
    """
    Display all books or filtered books if a search query is provided.
    Uses BookSearchForm to validate input safely and prevent SQL injection.
    """
    books = Book.objects.all()  # Default: show all books
    form = BookSearchForm(request.GET or None)

    if form.is_valid():
        query = form.cleaned_data['query']  # Cleaned and validated input
        # ORM query prevents SQL injection
        books = Book.objects.filter(title__icontains=query)

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})


def add_book(request):
    """
    Example form view for adding a book.
    CSRF-protected and validates input.
    """
    message = ''
    if request.method == 'POST':
        # Get and clean input
        title = request.POST.get('title', '').strip()
        if title:
            Book.objects.create(title=title)  # Safe ORM usage
            message = f'Book "{title}" added successfully.'
        else:
            message = 'Invalid title. Please enter a valid book name.'

    return render(request, 'bookshelf/form_example.html', {'message': message})


def book_detail(request, book_id):
