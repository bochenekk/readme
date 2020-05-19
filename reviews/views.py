# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.urls import reverse_lazy

from books.models import Book
from .models import Review


# Create your views here.
class AddReview(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'reviews/add_review.html'
    fields = ['title', 'content', 'grade']
    success_url = reverse_lazy('reviews:list-reviews')

    # def get_success_url(self): # określa co zrobić gdy formularz przeszedł walidację
    #     # i przekieruje na podaną stronę
    #     return reverse('books:book-details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Add review for book "{self.book}"',
        }
        context.update(kwargs)
        return super().get_context_data(**context)

    # nie trzeba zapisywać formularza bo CreateView to obsługuje (?)

    def get_book(self):
        book_id = self.kwargs.get('book_id')
        return get_object_or_404(Book, pk=book_id)

    def get(self, request, *args, **kwargs):
        self.book = self.get_book()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.book = self.get_book()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = self.book
        form.instance.state = 'draft'
        return super().form_valid(form)


class EditReview(LoginRequiredMixin, UpdateView):
    pk_url_kwarg = 'review_id'
    template_name = 'reviews/edit_review.html'
    fields = ['title', 'content', 'grade']
    success_url = reverse_lazy('reviews:list-reviews')

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Edit review "{self.object.title}" of book "{self.object.book}"',
        }
        context.update(kwargs)
        return super().get_context_data(**context)

    def get_queryset(self): # zamiast model = Review bo ograniczamy filtrem queryset
        return Review.objects.filter(user=self.request.user, state='draft')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = self.object.book
        form.instance.state = 'draft'
        return super().form_valid(form)


class PublishReview(LoginRequiredMixin, View):


    def post(self, request, *arg, **kwargs):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id, state='draft', user=request.user)
        review.state = 'in moderation'
        review.save()
        return redirect('reviews:list-reviews')


class ListReviews(LoginRequiredMixin, ListView):
    template_name = 'reviews/list_reviews.html'
    extra_context = {
        'title': 'Your reviews'
    }

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user).order_by('state', 'pub_date')
