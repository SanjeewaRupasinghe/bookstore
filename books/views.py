from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from books.models import Book,Review
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from books.forms import ReviewForm

class BookListView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        return Book.objects.all()

# def index(request):
#     data=Book.objects.all()
#     context={'data':data}
#     return render(request,'books/index.html',context)
    
class BookDetailsView(LoginRequiredMixin,DetailView):
    model=Book
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['review']=context['book'].review_set.order_by('-created_at')
        context['authors']=context['book'].authors.all()
        context['form']=ReviewForm
        return context

# def show(request,id):
#     book=get_object_or_404(Book,pk=id)
#     reviews=Review.objects.filter(book_id=id).order_by('-created_at')
#     context={'book':book,'reviews':reviews}
#     return render(request,'books/single-book.html',context)

def review(request):
    if request.user.is_authenticated:
        id=request.POST['id']
        record=Review(book_id=id,user=request.user)
        
        form=ReviewForm(request.POST,request.FILES,instance=record)
        if form.is_valid():
            form.save()
            
    return redirect(f"/books/{id}")

def author(request,author):
    books=Book.objects.filter(authors__name=author)
    context={'book_list':books}
    return render(request,'books/book_list.html',context)