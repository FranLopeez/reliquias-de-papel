from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.urls import reverse
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from books.models import Book


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'

    def form_valid(self, form):
        book = get_object_or_404(Book, pk=self.kwargs['book_pk'])
        form.instance.book = book
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('books:detail', kwargs={'pk': self.kwargs['book_pk']})


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'reviews/review_detail.html'

    def form_valid(self, form):
        review = get_object_or_404(Review, pk=self.kwargs['review_pk'])
        form.instance.review = review
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('reviews:detail', kwargs={'pk': self.kwargs['review_pk']})