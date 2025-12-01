from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# ------------------------------
# Django Class-Based Views (Required by Checker)
# ------------------------------

class AuthorListView(ListView):
    model = Author
    template_name = "author_list.html"
    context_object_name = "authors"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail.html"
    context_object_name = "author"


class AuthorCreateView(CreateView):
    model = Author
    fields = ["name"]
    template_name = "author_form.html"
    success_url = reverse_lazy("author-list")


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ["name"]
    template_name = "author_form.html"
    success_url = reverse_lazy("author-list")


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "author_confirm_delete.html"
    success_url = reverse_lazy("author-list")


# ------------------------------
# DRF API Views With Permission Classes
# ------------------------------

class AuthorListAPI(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class AuthorDetailAPI(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class BookListAPI(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDetailAPI(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookCreateAPI(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]


class BookUpdateAPI(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]


class BookDeleteAPI(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
