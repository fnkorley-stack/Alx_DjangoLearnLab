from rest_framework import serializers
from .models import Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'created_at', 'days_since_created']

    def get_days_since_created(self, obj):
        if obj.created_at:
            return (date.today() - obj.created_at.date()).days
        return None
