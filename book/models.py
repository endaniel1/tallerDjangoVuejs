from django.db import models

# Create your models here.

"""docstring for Book"""
class Book(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()