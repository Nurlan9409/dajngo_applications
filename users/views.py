from django.shortcuts import render
from django.http import HttpResponse

def users_page(request):
    return render(request, 'userss.html')


def about_page(request):
    return render(request, 'users1.html')
