from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=256)
    pageCount=models.IntegerField(default=0)
    thumbnailUrl=models.CharField(max_length=256,null=True)
    shortDescription=models.CharField(max_length=256,null=True)
    longDescription=models.TextField(null=True)
    longDescription=models.TextField(null=True)
    authors=models.ManyToManyField(Author)
    isbn=models.CharField(max_length=256,null=True)
    
    def __str__(self):
        return f"{self.id} {self.title}"

class Review(models.Model):
    body=models.TextField(max_length=256)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now=True)