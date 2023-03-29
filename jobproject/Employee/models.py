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
from django.urls import reverse


class Applylist(models.Model):
   cand=models.ForeignKey(Account,on_delete=models.CASCADE)
   job=models.ForeignKey(JobDetails,on_delete=models.CASCADE)
   education=models.CharField(max_length=200,default='')
   minsalary=models.CharField(max_length=20,default='')
   maxsalary=models.CharField(max_length=20,default='')
   resume=models.FileField(upload_to="resume")
   applieddate=models.DateTimeField(auto_now_add=True)
   status = models.BooleanField('status', default=True) 
   accept = models.BooleanField('accept', default=True) 
   reject = models.BooleanField('reject', default=True) 
   applied = models.BooleanField('applied', default=True)

   def __str__(self):
        return self.job.jobname




class SavedJobs(models.Model):
    id            = models.AutoField(primary_key=True)
    job = models.ForeignKey(JobDetails, related_name='saved_job', on_delete=models.CASCADE)
    user = models.ForeignKey(Account, related_name='saved', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    is_saved = models.BooleanField(default=False)

    def __str__(self):
        return self.job.jobname




class resume(models.Model):
    res_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,blank=True)
    position=models.CharField(max_length=200,blank=True)
    email=models.EmailField(max_length=100,blank=True, null=True)
    carobj=models.TextField(max_length=300,blank=True)
    college=models.CharField(max_length=200,blank=True)
    plus=models.CharField(max_length=200,blank=True)
    ten=models.CharField(max_length=200,blank=True)
    projects=models.TextField(max_length=100,blank=True)
    certi=models.TextField(max_length=100,blank=True)
    achi=models.TextField(max_length=100,blank=True)
    interns=models.TextField(max_length=100,blank=True)
    refe=models.TextField(max_length=100,blank=True)
    phone=models.TextField(max_length=100,blank=True, null=True)
    address=models.TextField(max_length=100,blank=True)
    strength=models.TextField(max_length=100,null=True,blank=True)
    skills=models.TextField(max_length=100,null=True,blank=True)
    lang=models.TextField(max_length=100,null=True,blank=True)
    hob=models.TextField(max_length=100,null=True,blank=True)
    soci=models.CharField(max_length=100,blank=True)
    coun=models.CharField(max_length=100,blank=True)
    status=models.BooleanField('status', default=0) 
    dob=models.DateField()
    gender=models.CharField(max_length=100,null=True)
    user_id=models.IntegerField(blank=True, null=True)

       
class Courses(models.Model):
    course=models.CharField(max_length=30,unique=True)
    duration = models.CharField(max_length=50,null=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    slug=models.SlugField()
    desc=models.TextField(max_length=200)
    start_date=models.DateField()
    end_date=models.DateField()
    last_date=models.DateField()
    userid=models.OneToOneField(Account,on_delete=models.CASCADE)

    class Meta:
        verbose_name="Courses"
        verbose_name_plural="Courses"

    def __str__(self):
        return self.course

    def get_course_url(self):
        return reverse('playcourse',kwargs={"c_slug":self.slug})

    def get_course_video_url(self):
        return reverse('playcourse',kwargs={"c_slug":self.slug})

    def endroll_check(self):
       if Course_purchase.objects.filter(course_id=self.id).exists():
           return False
       else:
           return True
       

class Videos(models.Model):
    title=models.CharField(max_length=300,unique=True)
    desp=models.TextField(max_length=3000,blank=True)
    slug=models.SlugField()
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    video=models.FileField(upload_to='videos')
    class Meta:
        verbose_name="Videos"
        verbose_name_plural="Videos"

    def __str__(self):
        return self.title

    def get_course_video_url(self):
        course_slug=Courses.objects.get(course=self.course).slug
        return reverse('playcourse',args=[course_slug,self.slug])


class Feedback(models.Model):
    userid=models.ForeignKey(Account,on_delete=models.CASCADE)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    
    feedback = models.TextField()
    feedbackdate = models.DateField(auto_now_add=True)


class Course_purchase(models.Model):
    userid=models.ForeignKey(Account,on_delete=models.CASCADE)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    purhase_date=models.DateField(auto_now=True)
    end_date=models.DateField(null=True)



