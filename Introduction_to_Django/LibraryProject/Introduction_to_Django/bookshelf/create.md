# Create Book Record

```python
from bookshelf.models import Book

# Create a new book record
Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book.save()
