
from django.shortcuts import render,redirect
from Account.models import Account
from Company.models import JobDetails
from Employee.models import Applylist,Courses



def index(request):
     
     Job=JobDetails.objects.all().order_by('date_posted')[:3]
     c = Courses.objects.all()
     context={
           'job_list':Job,
           'c': c,
           
          }
     return render(request,'index.html',context)




from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('comment')

        # Do something with the form data (e.g. send an email)

        # Render a success message
        return redirect('/')

    # If the request method is GET, render the contact form
    return render(request, 'contact.html')
