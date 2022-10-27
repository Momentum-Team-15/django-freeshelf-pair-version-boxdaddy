from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.bio.location.birth_date}"

class Resource(models.Model):
    title = models.TextField(max_length=50, blank=False)
    author = models.TextField(max_length=50, blank=False)
    description = models.TextField(max_length=200, blank=False)
    url = models.URLField(unique=True, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category", blank=True, null=True, on_delete=models.CASCADE, related_name="resources")

    def __str__(self):
        return f"{self.title} by {self.author}"

class Favorite(models.Model):
    created_at = models.DateTimeField(null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name
