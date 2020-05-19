from django.urls import path

from books import views


app_name = 'books'
urlpatterns = [
    # /
    path('', views.IndexView.as_view(), name='index'),
    # /books
    path('books', views.BookIndexView.as_view(), name='list-books'),
    # /books/<int:pk>
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-details'),
    # /authors
    path('authors', views.AuthorIndexView.as_view(), name='list-authors'),
    # /authors/<int:pk>
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-details'),
    # /categories
    path('categories', views.CategoryIndexView.as_view(), name='list-categories'),
    # /categories/<int:pk>
    path('categories/<int:pk>', views.CategoryDetailView.as_view(), name='category-details'),
]