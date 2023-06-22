from django.db import models
from django.db.models import BooleanField,CharField,ForeignKey,DateField,FloatField,EmailField,TextField,ManyToManyField

# Create your models here.
class Author(models.Model):
    Name=CharField(max_length=255)
    BirthDate=DateField()
    email=EmailField()

    def __str__(self) -> str:
        return self.Name
    

class Category(models.Model):
    Name=CharField(max_length=255)

    def __str__(self) -> str:   
        return self.Name

class Genre(models.Model):
    Name=CharField(max_length=255)

    def __str__(self) -> str:   
        return self.Name
    

class Book(models.Model):
    Title=CharField(max_length=255)
    author=ForeignKey(Author,on_delete=models.CASCADE)
    Publication_Date=DateField()
    Created_Date=DateField(auto_now_add=True)
    Is_Available=BooleanField(default=True)
    Price=FloatField()
    Description=TextField()
    Book_Code=CharField(max_length=15)
    category=ForeignKey(Category,on_delete=models.CASCADE)
    genre=ManyToManyField(Genre)
    Rating=FloatField()

    def __str__(self) -> str:
        return self.Title
    

    
