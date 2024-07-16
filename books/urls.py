from django.urls import path
from . import views

urlpatterns=[
    path('',views.BookListView.as_view(),name='book.all'),
    path('<int:pk>',views.BookDetailsView.as_view(),name='book.show'),
    path('<str:author>',views.author,name='author.books'),
    
    path('review',views.review,name='review.add')
]