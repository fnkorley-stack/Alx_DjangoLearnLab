```python
# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Verify the creation
book
# Expected output:
# <Book: 1984 by George Orwell (1949)>
