from django.db import models

from django.utils import timezone
from datetime import datetime
from distutils.command.upload import upload
from Account.models import Account
# Create your models here.

class JobDetails(models.Model):
    job_choices = (('Part-Time','Part-Time'),('Full-Time','Full-Time'),('Internship','Internship'),('Freelance','Freelance'))
    category_choices = (('Web Developers','Web Developers'),('Mobile Developers','Mobile Developers'),('Designers & Creatives','Designers & Creatives'),('Writers','Writers'),('Virtual Assistants','Virtual Assistants'), ('Accountants & Consultants','Accountants & Consultants'),('Sales & Marketing Experts','Sales & Marketing Experts'),('Customer Service Agents','Customer Service Agents'))
    id  = models.AutoField(primary_key=True)
    email= models.ForeignKey(Account,null=True,blank=True, on_delete=models.CASCADE)
    jobname=models.CharField(max_length=250,default='')
    companyname=models.CharField(max_length=250,default='')
    jobtype=models.CharField(max_length=250,choices=job_choices,default='')
    category=models.CharField(max_length=250,choices=category_choices,default='')
    companyaddress=models.CharField(max_length=250,default='')
    jobdescription=models.TextField(max_length=1500,default='')
    qualification=models.TextField(max_length=1500,default='')
    responsibility=models.TextField(max_length=1500,default='')
    location=models.CharField(max_length=250,default='')
    companywebsite=models.CharField(default='',max_length=20)
    companycontact=models.BigIntegerField(default=0)
    salarypackage=models.CharField(max_length=40,default='')
    experience=models.CharField(max_length=40,default='')
    tagline=models.CharField(max_length=100,default='')
    enddate=models.DateField(blank=True, null=True)
    logo=models.ImageField(upload_to="logos",null=True)
    date_posted = models.DateTimeField(default=timezone.now)



    
class Selected(models.Model):
    id            = models.AutoField(primary_key=True)
    job = models.ForeignKey(
    JobDetails, related_name='select_job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(Account, related_name='select_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant

   


