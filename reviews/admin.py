from django.contrib import admin
from .models import Review, Comment


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'book', 'author', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('title', 'content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'name', 'user', 'created_at')
    search_fields = ('name', 'content')
