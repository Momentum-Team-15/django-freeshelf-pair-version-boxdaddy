from django.contrib import admin
from .models import Resource, User, Favorite, Category

# Register your models here.

admin.site.register(Resource)
admin.site.register(User)
admin.site.register(Favorite)
admin.site.register(Category)