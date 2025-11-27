# vlogs/admin.py
from django.contrib import admin
from .models import VlogPost

@admin.register(VlogPost)
class VlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'category')
    list_filter = ('category', 'published_date', 'author')
    search_fields = ('title', 'description', 'tags', 'author__username')
    date_hierarchy = 'published_date'
