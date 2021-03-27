#Esta clase indica como vamos a pasar nuestro modelos por la red en este caso por xhml
from rest_framework import serializers
from .models import Book

"""docstring for BookSerializer"""
class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = "__all__"