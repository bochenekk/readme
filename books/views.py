from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Author, Book, Category


# Create your views here.
class BookIndexView(ListView):
    # queryset = Book.objects.all()
    model = Book
    template_name = "books/list_books.html"
    context_object_name = "books_list" # nazwa pola w kontekście
    # domyślnie wyniki zapisywane byłyby w object_list
    extra_context = {
        'title': 'List of Books'
    }


class AuthorIndexView(ListView):
    model = Author
    template_name = "books/list_authors.html"
    context_object_name = "authors_list"
    extra_context = {
        'title': 'List of Authors'
    }


class CategoryIndexView(ListView):
    model = Category
    template_name = "books/list_categories.html"
    context_object_name = "categories_list"
    extra_context = {
        'title': 'List of Categories'
    }