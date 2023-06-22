from django.urls import path
from . import views
from .views import AuthorView
urlpatterns=[
    path('',views.home,name='home'),
    path('booklist/',views.book_list,name='booklist'),
    path('bookdetails/<int:book_id>/',views.book_details,name='bookdetails'),
    path('authorlist/',AuthorView.as_view(),name='author_list'),
    path('createBook/',views.CreateBook,name='Create_Book'),
    path('createAuthor/',views.CreateAuthor.as_view(),name='Createauthor'),
    path('updatebook/<int:pk>/',views.CrUpdateBook.as_view(),name='Upbook'),

]
