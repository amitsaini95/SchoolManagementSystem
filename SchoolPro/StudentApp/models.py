from django.db import models
from SchoolApp.models import *
from BaseApp.models import User
# Create your models here.
GENDER=(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
)
class CourseModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class StudentProfileModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    studentClass=models.CharField(max_length=50)
    gender=models.CharField(max_length=10,choices=GENDER)
    course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,related_name="studentCourses",blank=True,null=True)
    phoneNo=models.IntegerField()
    schoolName=models.ForeignKey('SchoolApp.SchoolProfileModel', on_delete=models.CASCADE,related_name="schoolName",blank=True,null=True)
    email=models.EmailField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


