
from django.shortcuts import render
from django.http import HttpResponse
from .models import Courses

def course(request):
    var=Courses.objects.all()
    return render(request,'Courses/course.html',{'key1':var})

def singlecourse(request, id):
    Job=Courses.objects.filter(id=id)
    Job11=Courses.objects.get(id=id)

    context={
        'Job':Job,
       
    }
    return render(request,'Course/singlecourse.html',context)  
            