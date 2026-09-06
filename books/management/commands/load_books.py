from django.core.management.base import BaseCommand
from books.models import Book

BOOKS_DATA = [
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "publisher": "Chilton Books",
        "genre": "Ciencia ficción",
        "description": "Novela ambientada en el planeta desértico Arrakis, única fuente de la especia melange, el recurso más valioso del universo. Sigue a Paul Atreides, heredero de una casa noble, tras la traición que destruye a su familia y lo obliga a sobrevivir entre los Fremen del desierto.",
        "publication_date": "1965-08-01",
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "publisher": "Secker & Warburg",
        "genre": "Distopía",
        "description": "Retrata una sociedad totalitaria vigilada por el Gran Hermano, donde el Partido controla el pensamiento, reescribe la historia y persigue cualquier forma de disidencia. Sigue a Winston Smith, un funcionario que empieza a cuestionar el régimen.",
        "publication_date": "1949-06-08",
    },
    {
        "title": "La parábola del sembrador",
        "author": "Octavia E. Butler",
        "publisher": "Four Walls Eight Windows",
        "genre": "Ciencia ficción distópica",
        "description": "Ambientada en un Estados Unidos futuro en colapso social y ambiental, sigue a Lauren Olamina, una joven que desarrolla una nueva filosofía religiosa (Earthseed) mientras lidera a un grupo de sobrevivientes en busca de un lugar seguro.",
        "publication_date": "1993-01-01",
    },
    {
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "publisher": "Ballantine Books",
        "genre": "Distopía",
        "description": "En una sociedad donde los libros están prohibidos y los bomberos se dedican a quemarlos, un bombero empieza a cuestionar el sistema que sirve.",
        "publication_date": "1953-10-19",
    },
    {
        "title": "Un mundo feliz",
        "author": "Aldous Huxley",
        "publisher": "Chatto & Windus",
        "genre": "Distopía",
        "description": "Una sociedad futura controlada mediante el placer, el condicionamiento genético y la eliminación del sufrimiento, donde la libertad individual ha sido sacrificada por la estabilidad social.",
        "publication_date": "1932-01-01",
    },
]


class Command(BaseCommand):
    help = "Carga los libros iniciales del proyecto"

    def handle(self, *args, **kwargs):
        for data in BOOKS_DATA:
            book, created = Book.objects.get_or_create(
                title=data["title"], defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Creado: {book.title}"))
            else:
                self.stdout.write(f"Ya existía: {book.title}")