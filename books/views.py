from django.shortcuts import render
# from django.http import HttpResponse
import json

booksData=open("E:\\Projects\\python\\django_001\\bookstore\\books\\books.json").read()
data=json.loads(booksData)

def index(request):
    context={'data':data}
    return render(request,'books/index.html',context)
    # return HttpResponse('Book app')
    
def show(request,id):
    book=list()
    for d in data:
        if d['id']==id:
           book=d 

    context={'book':book}
    return render(request,'books/single-book.html',context)
