from django.urls import path, include

from . import views

app_name = 'library'

urlpatterns = [
    path('books/', views.BooKShow.as_view(), name="books_show"),
    path('book-detail/<int:pk>', views.BookDetail.as_view(), name="book_detail"),
    path('books/rent/<int:book_id>', views.RentBook, name="book_rent1"),
# path('books/rent/', views.RentBook2.as_view(), name="book_rent2"),

]
