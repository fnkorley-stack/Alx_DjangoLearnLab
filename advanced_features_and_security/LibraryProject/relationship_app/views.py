from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import user_passes_test, permission_required

from .forms import BookSearchForm  # Secure search form
from .models import Book, Library, UserProfile


# ---------------- BOOK LIST & SEARCH ----------------

def list_books(request):
    """
    Display all books or filter by search query.
    Uses BookSearchForm for input validation to prevent SQL injection.
    """
    books = Book.objects.all()
    form = BookSearchForm(request.GET or None)

    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)

    return render(request, "relationship_app/list_books.html", {"books": books, "form": form})


class ListBooksView(ListView):
    model = Book
    template_name = "relationship_app/list_books.html"
    context_object_name = "books"


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# ---------------- AUTHENTICATION ----------------

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')


# ---------------- ROLE-BASED ACCESS CONTROL ----------------

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == UserProfile.ROLE_ADMIN


def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == UserProfile.ROLE_LIBRARIAN


def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == UserProfile.ROLE_MEMBER


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")


# ---------------- CUSTOM PERMISSION-BASED CRUD ----------------

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author_id = request.POST.get("author", "").strip()

        if title and author_id:
            Book.objects.create(title=title, author_id=author_id)
            return redirect('list_books')
        else:
            message = "Invalid input."
            return render(request, 'relationship_app/add_book.html', {"message": message})

    return render(request, 'relationship_app/add_book.html')


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author_id = request.POST.get("author", "").strip()

        if title and author_id:
            book.title = title
            book.author_id = author_id
            book.save()
            return redirect('list_books')
        else:
            message = "Invalid input."
            return render(request, 'relationship_app/edit_book.html', {"book": book, "message": message})

    return render(request, 'relationship_app/edit_book.html', {"book": book})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect('list_books')

    return render(request, 'relationship_app/delete_book.html', {"book": book})
