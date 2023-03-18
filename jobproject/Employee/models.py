import datetime
from unittest.util import _MAX_LENGTH
from django.db import models
from Account.models import Account
from Company.models import JobDetails
from django_countries.fields import CountryField
# Create your models here.
from django.utils import timezone
from datetime import datetime
from distutils.command.upload import upload


class Applylist(models.Model):
   cand=models.ForeignKey(Account,on_delete=models.CASCADE)
   job=models.ForeignKey(JobDetails,on_delete=models.CASCADE)
   education=models.CharField(max_length=200,default='')
   minsalary=models.CharField(max_length=20,default='')
   maxsalary=models.CharField(max_length=20,default='')
   resume=models.FileField(upload_to="resume")
   applieddate=models.DateTimeField(auto_now_add=True)




class SavedJobs(models.Model):
    id            = models.AutoField(primary_key=True)
    job = models.ForeignKey(JobDetails, related_name='saved_job', on_delete=models.CASCADE)
    user = models.ForeignKey(Account, related_name='saved', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.title


class AppliedJobs(models.Model):
    id            = models.AutoField(primary_key=True)
    job = models.ForeignKey( JobDetails, related_name='applied_job', on_delete=models.CASCADE)
    user = models.ForeignKey( Account, related_name='applied_user', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.title



class resume(models.Model):
    res_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,blank=True)
    position=models.CharField(max_length=100,blank=True)
    email=models.EmailField(blank=True, null=True)
    carobj=models.TextField(blank=True)
    college=models.CharField(max_length=100,blank=True)
    plus=models.CharField(max_length=100,blank=True)
    ten=models.CharField(max_length=100,blank=True)
    projects=models.TextField(blank=True)
    certi=models.TextField(blank=True)
    achi=models.TextField(blank=True)
    interns=models.TextField(blank=True)
    refe=models.TextField(blank=True)
    phone=models.IntegerField(blank=True, null=True,default=0)
    address=models.TextField(blank=True)
    strength=models.TextField(null=True,blank=True)
    skills=models.TextField(null=True,blank=True)
    lang=models.TextField(null=True,blank=True)
    hob=models.TextField(null=True,blank=True)
    soci=models.CharField(max_length=100,blank=True)
    coun=models.CharField(max_length=100,blank=True)
    status=models.BooleanField('status', default=0) 
    dob=models.DateField()
    gender=models.CharField(max_length=100,null=True)
    user_id=models.IntegerField(blank=True, null=True)


