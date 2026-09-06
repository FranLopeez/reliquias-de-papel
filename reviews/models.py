from django.db import models
from django.conf import settings
from books.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator



class Review(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )  # ej: 1 a 5
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.book.title})"


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.name} on {self.review.title}"
