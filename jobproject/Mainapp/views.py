

from django.shortcuts import render,redirect
from Account.models import Account
from Company.models import JobDetails
from Employee.models import Applylist,Courses

from django.contrib import messages

def index(request):
     
     Job=JobDetails.objects.all().order_by('date_posted')[:3]
     c = Courses.objects.all()
     context={
           'job_list':Job,
           'c': c,
           
          }
     return render(request,'index.html',context)




from django.views.decorators.csrf import csrf_exempt

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def contact(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('comment')

        # Create a message object
     #    msg = MIMEMultipart()
     #    msg['From'] = email
     #    msg['To'] = 'jobseekingajce@gmail.com'  # Replace with your own email address
     #    msg['Subject'] = f"New message from {name}"

     #    # Add the message body
     #    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
     #    msg.attach(MIMEText(body, 'plain'))

     #    # Send the message
     #    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
     #        smtp.starttls()
     #        smtp.login('jobseekingajce@gmail.com', 'jobportal123')  # Replace with your own email credentials
     #        smtp.send_message(msg)

        # Render a success message
        messages.success(request,'Message sent Successfully')
        return redirect('/')

    # If the request method is GET, render the contact form
    return render(request, 'contact.html')

