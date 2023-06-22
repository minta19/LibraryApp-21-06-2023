from django.contrib import admin
from .models import Author
from .models import Category
from .models import Genre
from .models import Book
# Register your models here.

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Book)
