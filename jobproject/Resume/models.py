import datetime
from unittest.util import _MAX_LENGTH
from django.db import models
from Account.models import Account

from django_countries.fields import CountryField
# Create your models here.
from django.utils import timezone
from datetime import datetime
from distutils.command.upload import upload



class resumme(models.Model):
    res_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,blank=True)
    position=models.CharField(max_length=100,blank=True)
    email=models.EmailField(blank=True, null=True)
    carobj=models.TextField(blank=True)
    college=models.CharField(max_length=100,blank=True)
    colcourse=models.CharField(max_length=100,blank=True)
    colpy=models.CharField(max_length=100,blank=True)
    plus=models.CharField(max_length=100,blank=True)
    plusmarks=models.CharField(max_length=100,blank=True)
    pluspy=models.CharField(max_length=100,blank=True)
    ten=models.CharField(max_length=100,blank=True)
    schomarks=models.CharField(max_length=100,blank=True)
    schopy=models.CharField(max_length=100,blank=True)
    refe=models.TextField(blank=True,null=True)
    phone=models.BigIntegerField(default=0)
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
    user_id=models.ForeignKey(Account, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

class interdetails(models.Model):
    in_id=models.AutoField(primary_key=True)
    cann_id=models.IntegerField(blank=True, null=True)
    status=models.BooleanField('status', default=False) 
    interns=models.CharField(max_length=100,null=True)
    internname=models.CharField(max_length=100,null=True)
    interndate=models.DateField()

class projectdetails(models.Model):
    pro_id=models.AutoField(primary_key=True)
    cann_id=models.IntegerField(blank=True, null=True)
    status=models.BooleanField('status', default=False) 
    proname=models.CharField(max_length=100,null=True)
    prodetails=models.CharField(max_length=100,null=True)
    

class achidetails(models.Model):
    achi_id=models.AutoField(primary_key=True)
    cann_id=models.IntegerField(blank=True, null=True)
    status=models.BooleanField('status', default=False) 
    achiname=models.CharField(max_length=100,null=True)
    achiinfo=models.CharField(max_length=100,null=True)
    achidate=models.DateField()

class certidetails(models.Model):
    cer_id=models.AutoField(primary_key=True)
    cann_id=models.IntegerField(blank=True, null=True)
    status=models.BooleanField('status', default=False) 
    certiname=models.CharField(max_length=100,null=True)
    cerinfo=models.CharField(max_length=100,null=True)
    certidate=models.DateField()