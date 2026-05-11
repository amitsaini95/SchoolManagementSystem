from django.db import models
from SchoolApp.models import *
from BaseApp.models import User
# Create your models here.
GENDER=(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
)
class StudentProfileModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    studentClass=models.CharField(max_length=50)
    gender=models.CharField(max_length=10,choices=GENDER)
    phoneNo=models.IntegerField()
    schoolName=models.ForeignKey('SchoolApp.SchoolProfileModel', on_delete=models.CASCADE,related_name="schoolName",blank=True,null=True)
    email=models.EmailField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
class Attendance(models.Model):
    student=models.ForeignKey(StudentProfileModel,on_delete=models.CASCADE,null=True,blank=True)
    dateTime=models.DateTimeField(auto_now=True)


    
