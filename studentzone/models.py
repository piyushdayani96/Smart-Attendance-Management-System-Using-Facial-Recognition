from django.db import models

# Create your models here.
class Question(models.Model):
    qid=models.AutoField(primary_key=True)
    questiontext=models.TextField()
    askedby=models.CharField(max_length=50)
    pasteddate=models.CharField(max_length=30)
class Answer(models.Model):
    aid=models.AutoField(primary_key=True)
    answertext=models.TextField()
    answeredby=models.CharField(max_length=50)
    qid=models.IntegerField()
    answereddate=models.CharField(max_length=30)
class Complain(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    rollno=models.CharField(max_length=15)
    contactno=models.CharField(max_length=15)
    subject=models.CharField(max_length=200)
    complaintext=models.TextField()
    complaindate=models.CharField(max_length=30)