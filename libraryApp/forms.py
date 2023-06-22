from django.forms import ModelForm
from .models import Book,Author


class BookCreate(ModelForm):
    class Meta:
        model=Book
        fields='__all__'

class AuthorCreate(ModelForm):
    class Meta:
        model=Author
        fields='__all__'

class UpdateBook(ModelForm):
    class Meta:
        model=Book
        fields=['Title','Is_Available']