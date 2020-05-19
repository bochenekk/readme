from django.shortcuts import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import AccessMixin
from django.views.generic.detail import SingleObjectMixin # ma zaimplementowane
# metody do pobierania pojedynczego elementu
# np get. Rodzic (jeden z) FormView

from django.db.models import Avg, Count

from reviews.forms import GradeForm
from .models import Author, Book, Category
# from reviews.models import Grade


class IndexView(TemplateView):
    template_name = "index.html"
    extra_context = {
        'title': "Homepage",
    }

    # def get_context_data(self, **kwargs):
    #     context = {
    #         'best_book': Book.object.filter().order_by()
    #     }
    #     context.update(kwargs)
    #     return super().context_data(**context)


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


class BookDetailView(AccessMixin, SingleObjectMixin, FormView): # SingleObjectMixin obsługuje pobieranie np książki po ID
    model = Book
    template_name = "books/book_details.html"
    form_class = GradeForm

    def get_success_url(self): # określa co zrobić gdy formularz przeszedł walidację
        # i przekieruje na podaną stronę
        return reverse('books:book-details', kwargs={'pk': self.object.pk})

    def get(self, request, *args, **kwargs): # reaguje na żądanie typu GET
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs): # reaguje na żądanie typu POST
        if not request.user.is_authenticated:
            return self.handle_no_permission() # zdefiniowane w auth.mixins import AccessMixin
        self.object = self.get_object() # self.object będzie potem używany w get_succes_url i context
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = self.object # self.book
        self.grade = form.save() # stworzy nowy obiekt w bazie danych
        return super().form_valid(form)
        #ta metoda zastępuje get_initial()

    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['user'] = self.request.user
    #     initial['book'] = self.object
    #     return initial

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Book {self.object.title} by {self.object.author}',
            'avg_grades': self.object.grade_set.aggregate(
                average=Avg('grade'), count=Count('grade')
                ),
            # 'next': self.request.path, # gdyby chcieć korzystać z if next w comments/form.html
        }
        context.update(kwargs)
        return super().get_context_data(**context)


class AuthorIndexView(ListView):
    model = Author
    template_name = "books/list_authors.html"
    context_object_name = "authors_list"
    extra_context = {
        'title': 'List of Authors'
    }


class AuthorDetailView(DetailView):
    model = Author
    template_name = "books/author_details.html"
    # extra_context = {
    #     'title': 'Author'
    # }

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Author: {self.object}',
            # 'next': self.request.path, # gdyby chcieć korzystać z if next w comments/form.html
        }
        context.update(kwargs)
        return super().get_context_data(**context)


class CategoryIndexView(ListView):
    model = Category
    template_name = "books/list_categories.html"
    context_object_name = "categories_list"
    extra_context = {
        'title': 'List of Categories'
    }


class CategoryDetailView(DetailView):
    model = Category
    template_name = "books/category_details.html"
    context_object_name = "category"
    # extra_context = {
    #     'title': 'Category'
    # }

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Category {self.object}',
        }
        context.update(kwargs)
        return super().get_context_data(**context)