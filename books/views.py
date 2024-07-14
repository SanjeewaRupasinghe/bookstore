from django.shortcuts import render
from books.models import Book
# from django.http import HttpResponse

def index(request):
    data=Book.objects.all()
    context={'data':data}
    return render(request,'books/index.html',context)
    # return HttpResponse('Book app')
    
def show(request,id):
    book=Book.objects.filter(id=id).first()
    context={'book':book}
    return render(request,'books/single-book.html',context)
