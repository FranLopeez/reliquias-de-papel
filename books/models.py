from django.db import models
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    publisher = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    publication_date = models.DateField(null=True, blank=True)


    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title} — {self.author}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.created_at:%d/%m/%Y}"