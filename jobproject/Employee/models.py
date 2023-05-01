import datetime
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import ValidationError
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
   resumes= models.FileField(upload_to='AppliedResume',blank=True, null=True)
   applieddate=models.DateTimeField(auto_now_add=True)
   status_choices = [
        ('PENDING', 'Pending'),
        ('REJECTED', 'Rejected'),
        ('ACCEPTED', 'Accepted')
    
    ]
   status = models.CharField(max_length=8, choices=status_choices, default='PENDING')
   notes = models.TextField(blank=True, null=True)




class SavedJobs(models.Model):
    id            = models.AutoField(primary_key=True)
    job = models.ForeignKey(JobDetails, related_name='saved_job', on_delete=models.CASCADE)
    user = models.ForeignKey(Account, related_name='saved', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    is_saved = models.BooleanField(default=False)

    def __str__(self):
        return self.job.jobname




       
class Courses(models.Model):
    course=models.CharField(max_length=30,unique=True)
    duration = models.CharField(max_length=50,null=True)
    amount=models.PositiveIntegerField(default=100)
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
    def clean(self):
        today = timezone.now().date()
        if self.start_date and self.start_date < today:
            raise ValidationError(_('Start date cannot be in the past.'))
        if self.end_date and self.end_date < today:
            raise ValidationError(_('End date cannot be in the past.'))
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError(_('End date must be after start date.'))

        # Don't forget to call the parent class's clean method!
        super().clean()   

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



class sentiment(models.Model):
    review = models.ForeignKey(Feedback,on_delete=models.CASCADE)
    positive_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    positive_percentage = models.DecimalField(max_digits=5,decimal_places=2, null=True)
    negative_percentage = models.DecimalField(max_digits=5,decimal_places=2, null=True)
    neutral_percentage = models.DecimalField(max_digits=5,decimal_places=2, null=True)
    compoud_score = models.DecimalField(max_digits=5,decimal_places=2, null=True)
    num_reviews = models.IntegerField(default=0)    
   


class Course_purchase(models.Model):
    userid=models.ForeignKey(Account,on_delete=models.CASCADE)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    purhase_date=models.DateField(auto_now=True)
    end_date=models.DateField(null=True)

class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField(blank=True,null=True)
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user)

