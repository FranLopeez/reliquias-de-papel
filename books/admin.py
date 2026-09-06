from django.contrib import admin
from .models import Book, ContactMessage


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publisher', 'publication_date')
    search_fields = ('title', 'author')
    list_filter = ('genre', 'publisher')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')