from django.shortcuts import render
from django.views import View

from users.models import Student


class StudentLisView(View):
    def get(self,request):
        students = Student.objects.all()
        return render(request,'student.html',{'students':students})



class MainView(View):
    def get(self, request):
        return render(request, 'main.html')