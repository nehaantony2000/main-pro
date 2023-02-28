from django.db import models

from django.urls import reverse
# Create your models here.

class Courses(models.Model):
    id  = models.AutoField(primary_key=True)
    image=models.ImageField(upload_to='pics')
    title=models.CharField(max_length=250)
    desp=models.TextField()
    date=models.DateField()
    