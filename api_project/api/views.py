from rest_framework import generics, viewsets        # ← added viewsets
from rest_framework.permissions import IsAuthenticated   # ← needed for permission_classes
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):           # ← now works
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
