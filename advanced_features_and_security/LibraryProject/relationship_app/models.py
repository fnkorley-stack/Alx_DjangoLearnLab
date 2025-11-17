from django.db import models
from django.conf import settings

# Author model
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


# Library model
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name


# UserProfile model
class UserProfile(models.Model):
    ROLE_MEMBER = 'Member'
    ROLE_LIBRARIAN = 'Librarian'

    ROLE_CHOICES = [
        (ROLE_MEMBER, 'Member'),
        (ROLE_LIBRARIAN, 'Librarian'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_MEMBER)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Librarian model
class Librarian(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='librarians')

    def __str__(self):
        return self.name
