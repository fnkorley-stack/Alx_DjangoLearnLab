from django.urls import path
from . import views

urlpatterns = [
    # ------------------------------
    # BOOK LIST & DETAIL
    # ------------------------------
    path('list_books/', views.list_books, name='list_books'),
    path('list_books_class/', views.ListBooksView.as_view(), name='list_books_class'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # ------------------------------
    # AUTHENTICATION
    # ------------------------------
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ------------------------------
    # ROLE-BASED ACCESS CONTROL
    # ------------------------------
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),

    # ------------------------------
    # PERMISSION-BASED CRUD
    # ------------------------------
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
