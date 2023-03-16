# from django.db import models
# from Account.models import Account
# from django.urls import reverse
# Create your models here.

# class Courses(models.Model):
#     id  = models.AutoField(primary_key=True)
#     image=models.ImageField(upload_to='pics')
#     title=models.CharField(max_length=250)
#     desp=models.TextField()
#     date=models.DateField()
    
# class Courses(models.Model):
#     course=models.CharField(max_length=30,unique=True)
#     duration = models.CharField(max_length=50,null=True)
#     amount = models.DecimalField(max_digits=10,decimal_places=2)
#     slug=models.SlugField()
#     desc=models.TextField(max_length=200)
#     start_date=models.DateField()
#     end_date=models.DateField()
#     user_id=models.OneToOneField(Account,on_delete=models.CASCADE)

#     class Meta:
#         verbose_name="Courses"
#         verbose_name_plural="Courses"

#     def __str__(self):
#         return self.course

#     def get_course_url(self):
#         return reverse('Employee:userhome',kwargs={"c_slug":self.slug})

#     def get_course_video_url(self):
#         return reverse('Employee:userhome',kwargs={"c_slug":self.slug})

#     def endroll_check(self):
#        if Course_purchase.objects.filter(course_id=self.id).exists():
#            return False
#        else:
#            return True
       

# class Videos(models.Model):
#     title=models.CharField(max_length=30,unique=True)
#     slug=models.SlugField()
#     course=models.ForeignKey(Courses,on_delete=models.CASCADE)
#     video=models.FileField(upload_to='videos')
#     class Meta:
#         verbose_name="Videos"
#         verbose_name_plural="Videos"

#     def __str__(self):
#         return self.title

#     def get_course_video_url(self):
#         course_slug=Courses.objects.get(course=self.course).slug
#         return reverse('Employee:userhome',args=[course_slug,self.slug])


# class Feedback(models.Model):
#     user=models.OneToOneField(Account,on_delete=models.CASCADE)
#     course=models.ForeignKey(Courses,on_delete=models.CASCADE)
#     feedback = models.TextField()
#     feedbackdate = models.DateField(auto_now_add=True)


# class Course_purchase(models.Model):
#     user=models.ForeignKey(Account,on_delete=models.CASCADE)
#     course=models.ForeignKey(Courses,on_delete=models.CASCADE)
#     purhase_date=models.DateField(auto_now=True)
#     end_date=models.DateField(null=True)
