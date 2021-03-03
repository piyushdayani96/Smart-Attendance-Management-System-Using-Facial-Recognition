from django.db import models
class Department(models.Model):
    deptname=models.CharField(max_length=50)
    deptcode=models.CharField(max_length=10)
    depthod=models.CharField(max_length=70)
    course=models.CharField(max_length=50)
class Subject(models.Model):
    subjectname=models.CharField(max_length=50)
    semester=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    subjectcode=models.CharField(max_length=50)
    teachername=models.CharField(max_length=50)
    studentgroup=models.CharField(max_length=50)
    attendanceDateTime=models.CharField(max_length=50)



