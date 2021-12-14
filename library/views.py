from django.shortcuts import render
from django.urls import reverse

from persons.models import Student
from .models import *
# Create your views here.
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden, HttpResponseRedirect
from django.views import generic, View
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Rent_Form


# students = [student.username for student in list(Student.objects.all())]
class BooKShow(LoginRequiredMixin,generic.ListView):
    model = Book
    template_name = 'library/books.html'
    def get_queryset(self):
        # if self.request.user.username in students:
        #     return Book.objects.filter(students__username=self.request.user.username)
        # else:
        return Book.objects.all()


class BookDetail(LoginRequiredMixin,generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = "book"


def RentBook(request,book_id):
    book = Book.objects.filter(pk=book_id).first()
    if request.method == 'POST':
        form = Rent_Form(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']  # variable to store cleaned data
            end_date = form.cleaned_data['end_date']
            rent = Rent(book=book,start_date=start_date, end_date=end_date)
            rent.save()
            book.is_rent=True
            book.save()
            stu=Student.objects.filter(username=request.user.username).first()
            stu.rented_book.add(rent)

    else:

        data = {'book': book.name}
        form = Rent_Form(data)
    return render(request, 'library/book_rent.html', {'form': form, 'book': book})
