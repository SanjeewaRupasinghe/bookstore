from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404,redirect
from books.models import Book,Review
from django.http import Http404
from django.views.generic import ListView

class BookListView(ListView):
    def get_queryset(self):
        return Book.objects.all()

# def index(request):
#     data=Book.objects.all()
#     context={'data':data}
#     return render(request,'books/index.html',context)
    
def show(request,id):
    book=get_object_or_404(Book,pk=id)
    reviews=Review.objects.filter(book_id=id).order_by('-created_at')
    context={'book':book,'reviews':reviews}
    return render(request,'books/single-book.html',context)

def review(request):
    id=request.POST['id']
    review=request.POST['review']
    
    record=Review(body=review,book_id=id)
    record.save()
    return redirect('/books')