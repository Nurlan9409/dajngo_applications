from django.urls import path
from .views import Book_lisView,Book_detailView


urlpatterns = [
    path('library/', Book_lisView.as_view(), name='library'),
    path('book_detail/<int_id>',Book_detailView.as_view(), name='book_detail')
]