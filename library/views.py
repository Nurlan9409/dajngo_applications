from django.shortcuts import render

from django.views import View
from .models import Book
from django.http import HttpResponse

class Book_lisView(View):
     def get(self,request):
          search = request.GET.get('search')
          books = Book.objects.filter(title__icontains=search)
          if books.count() != 0:

                context = {'books':books}
                return render(request,'librarys.html',context)
          else:
               return HttpResponse("Not found")
class Book_detailView(View):
     def get(self,request):
          book = Book.objects.get(id=id)
          return render(request,'book_detail.html',{'book':book})