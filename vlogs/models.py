from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class VlogPost(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the vlog")
    video_url = models.URLField(help_text="URL of the vlog video")
    description = models.TextField(blank=True, help_text="Description of the vlog")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, help_text="Author of the vlog")
    published_date = models.DateTimeField(auto_now_add=True, help_text="Date published")
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, help_text="Category of the vlog")

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
