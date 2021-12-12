from django.db import models
from rest_framework import generics
from .serializers import BooksSerializer
from .models import Book

class BooksListView(generics.ListCreateAPIView):    
    serializer_class = BooksSerializer
    queryset = Book.objects.all()

class BooksDetailView(generics.RetrieveAPIView):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()
