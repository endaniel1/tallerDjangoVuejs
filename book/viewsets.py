#Esta clase permitira realizar nuestro crud a nuestro models
from rest_framework import viewsets

from .models import Book

from .serializer import BookSerializer

"""docstring for BookViewSet"""
class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
