# Django Admin Setup for Bookshelf App

## Step 1: Register the Book Model
In `bookshelf/admin.py`, the Book model was registered with the Django admin interface using the following code:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
