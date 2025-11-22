from django.contrib import admin
from .models import Book

# --------------------
# ADMIN FOR BOOK MODEL
# --------------------
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
