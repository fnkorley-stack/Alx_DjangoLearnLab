# Create Book Record

```python
from bookshelf.models import Book

# Create a new book record
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Save the book (though .create() already saves automatically)
book.save()
