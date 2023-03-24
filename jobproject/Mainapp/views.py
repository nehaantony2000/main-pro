
from django.shortcuts import render
from Account.models import Account
from Company.models import JobDetails
from Employee.models import Applylist,Courses



def index(request):
     
     Job=JobDetails.objects.all()
     c = Courses.objects.all()
     context={
           'job_list':Job,
           'c': c,
           
          }
     return render(request,'index.html',context)

def contact(request):
    
    return render(request,'contact.html')



