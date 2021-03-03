from django.db import models
class Studentgroup(models.Model):
    teachername=models.CharField(max_length=50)
    studentgroup=models.CharField(max_length=50)
    startroll=models.IntegerField(max_length=50,default=0)
    endroll=models.IntegerField(max_length=50,default=0)
    startrolllate=models.IntegerField(max_length=50,default=0)
    endrolllate=models.IntegerField(max_length=50,default=0)


# Create your models here.
