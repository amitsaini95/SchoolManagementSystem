from django.db import models
from SchoolApp.models import *
from BaseApp.models import User
from TeacherApp.models import TeacherProfileModel
# Create your models here.

GENDER=(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
)
seniorClass=(
    ('XI','XI'),
    ('XII','XII')
)

class SessionModel(models.Model):
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return "From " + str(self.start_year) + " to " + str(self.end_year)
class CourseModel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class StudentProfileModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField(null=True)
    steamClass=models.CharField(max_length=10,choices=seniorClass)
    gender=models.CharField(max_length=10,choices=GENDER)
    course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,related_name="studentCourses",blank=True,null=True)
    phoneNo=models.IntegerField(null=True)
    schoolName=models.ForeignKey('SchoolApp.SchoolProfileModel', on_delete=models.CASCADE,related_name="schoolName",blank=True,null=True)
    email=models.EmailField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class SubjectModel(models.Model):

    name = models.CharField(max_length=255)
    course = models.ForeignKey('CourseModel', on_delete=models.DO_NOTHING, null=True, blank=False)
    session = models.ForeignKey('SessionModel', on_delete=models.DO_NOTHING, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.course.name

  

    

class AttendanceReport(models.Model):
    staff=models.ForeignKey('TeacherApp.TeacherProfileModel', on_delete=models.CASCADE)
    student = models.ForeignKey('StudentProfileModel', on_delete=models.DO_NOTHING)
    subject=models.ForeignKey('SubjectModel',on_delete=models.CASCADE)
    attendanceDate=models.DateField()
    status = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user} on {self.attendanceDate} date"
    