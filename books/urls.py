from django.urls import path
from . import views

urlpatterns=[
    path('',views.BookListView.as_view(),name='book.all'),
    path('<int:id>',views.show,name='book.show'),
    
    path('review',views.review,name='review.add')
]