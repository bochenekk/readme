from django.urls import path

from books import views


app_name = 'books'
urlpatterns = [
    # /books
    path('books', views.BookIndexView.as_view(), name='list_books'),
    # /authors
    path('authors', views.AuthorIndexView.as_view(), name='list_authors'),
    # /categories
    path('categories', views.CategoryIndexView.as_view(), name='list_categories'),
]