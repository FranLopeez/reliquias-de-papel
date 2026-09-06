from django.core.management.base import BaseCommand
from books.models import Book

BOOKS_DATA = [
    {
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "publisher": "Ballantine Books",
        "genre": "Distopía",
        "description": "En una sociedad donde los libros están prohibidos...",
        "publication_date": "1953-10-19",
    },
    {
        "title": "Un mundo feliz",
        "author": "Aldous Huxley",
        "publisher": "Chatto & Windus",
        "genre": "Distopía",
        "description": "Una sociedad futura controlada mediante placer...",
        "publication_date": "1932-01-01",
    },
]


class Command(BaseCommand):
    help = "Carga libros de ejemplo en la base de datos"

    def handle(self, *args, **kwargs):
        for data in BOOKS_DATA:
            book, created = Book.objects.get_or_create(
                title=data["title"], defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Creado: {book.title}"))
            else:
                self.stdout.write(f"Ya existía: {book.title}")