from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'rating', 'release_date', 'created_at']
    list_filter = ['genre', 'release_date']
    search_fields = ['title', 'description']
    ordering = ['-created_at']