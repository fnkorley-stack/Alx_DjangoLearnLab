from django.db import models

# Author model: stores basic author information
class Author(models.Model):
    # The author's full name
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model: stores book information and links to an Author
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=255)

    # Year the book was published
    publication_year = models.IntegerField()

    # A ForeignKey establishes a one-to-many relationship:
    # One Author can have MANY Books.
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
