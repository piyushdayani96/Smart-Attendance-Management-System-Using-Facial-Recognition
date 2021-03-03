from django.db import models
from django.utils import timezone


# Create your models here.
class LoginInfo(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=20)

class StudentInfo(models.Model):
    name=models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    address=models.TextField()
    branch=models.CharField(max_length=50)
    semester=models.IntegerField(default=0)
    contactno=models.CharField(max_length=50)
    emailaddress=models.CharField(max_length=50)
    rollno=models.CharField(max_length=50,primary_key=True,default=0)
    password=models.CharField(max_length=20)
    connectdate = models.DateField(default=timezone.now)
    file= models.FileField(upload_to='images/')

class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    address=models.TextField()
    contact_no=models.CharField(max_length=15)
    emailaddress=models.EmailField()
    enquirytext=models.TextField()
    enquirydate=models.CharField(max_length=20)