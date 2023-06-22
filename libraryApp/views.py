from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView
from .forms import BookCreate,AuthorCreate,UpdateBook
from .models import Book
# Create your views here.
def home(request):
    return render(request,'libraryApp/home.html')

def book_list(request):
    all_books=Book.objects.all()
    context={
        "allbook":all_books
    }
    return render(request,'libraryApp/book_list.html',context)

def book_details(request,book_id):
    try:
       details=Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponse("book not found")
       
             
    return render(request,'libraryApp/book_details.html',{"Books":details})
       
     
class AuthorView(ListView):
    template_name = 'libraryapp/author_list.html'
    queryset=Book.objects.all()
    context_object_name="allbook"


def CreateBook(request):
    form=BookCreate()
    if request.method == 'POST':
        form=BookCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Create_Book')
    context={"form":form}
    return render(request,'libraryApp/create_book.html',context)

class CreateAuthor(CreateView):
    template_name='libraryApp/author_create.html'
    form_class=AuthorCreate
    def get_success_url(self) -> str:
        return reverse('Createauthor')
    
class CrUpdateBook(UpdateView):
    model=Book
    template_name='libraryApp/book_update_form.html'
    template_name_suffix = "_update_form"
    form_class=UpdateBook
    def get_success_url(self) -> str:
        return reverse('Upbook',kwargs={'pk': self.object.pk})

