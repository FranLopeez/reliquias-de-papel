from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from django.db.models import Q
from django.contrib import messages
from .models import Book
from .forms import ContactForm


def home(request):
    return render(request, 'books/home.html')


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        queryset = Book.objects.all()
        query = self.request.GET.get('q')
        genre = self.request.GET.get('genre')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(author__icontains=query)
            )
        if genre:
            queryset = queryset.filter(genre=genre)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Book.objects.order_by('genre').values_list('genre', flat=True).distinct()
        context['current_query'] = self.request.GET.get('q', '')
        context['current_genre'] = self.request.GET.get('genre', '')
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class ContactView(FormView):
    template_name = 'books/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('books:contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, '¡Gracias! Tu mensaje fue enviado correctamente.')
        return super().form_valid(form)